"""The three interaction modes. Each one uses different instructions, context and tools."""
import re
import textwrap

from . import config
from .citations import check_citations
from .evidence import run_header, save_run
from .model import LocalGemma
from .prompts import ask_messages, chat_messages
from .retrieval import load_index


def print_passages(passages):
    for i, p in enumerate(passages, 1):
        print(f"\n[S{i}] score {p['score']}  {p['path']} > {p['heading']}")
        print(textwrap.indent(p["text"], "    "))


# ---------- search: retrieval only, no model ----------

def run_search(query, k, include_wiki):
    index = load_index()
    passages = index.search(query, k=k, kind=None if include_wiki else "source")
    if not passages:
        print("No matching passages.")
    print_passages(passages)
    path = save_run("search", {**run_header("search"), "query": query, "passages": passages})
    print(f"\nSaved: {path.relative_to(config.ROOT)}")


# ---------- ask: standalone RAG with citations ----------

def run_ask(question, k):
    """Retrieve evidence, send it with the research rules to Gemma, check the citations.
    Takes only the question: no chat history and no persona can reach this function."""
    index = load_index()
    passages = index.search(question, k=k, kind="source")
    best = passages[0]["score"] if passages else 0.0
    stats = {}
    if best < config.ASK_MIN_SCORE:
        answer = "Insufficient evidence: no passage in my sources matches this question."
        gemma_called = False
    else:
        gemma = LocalGemma()
        answer = gemma.generate(ask_messages(question, passages),
                                config.ASK_MAX_TOKENS, config.ASK_TEMPERATURE)
        stats = {"model_load_seconds": gemma.load_seconds, **gemma.last}
        gemma_called = True
    citations = check_citations(answer, passages)

    print("\nRetrieved passages:")
    print_passages(passages)
    print(f"\nAnswer ({config.MODEL_ID}, local):\n{answer}\n")
    print(f"Citation check: {citations['status']}")
    for c in citations["cited"]:
        print(f"  {c['label']} = {c['path']} > {c['heading']}")
    if stats:
        print(f"Response time: {stats['response_seconds']} s, peak model memory: {stats['peak_model_memory_gb']} GB")
    record = {**run_header("ask"), "query": question, "passages": passages, "answer": answer,
              "citations": citations, "stats": stats,
              "details": {"best_score": best, "gemma_called": gemma_called}}
    path = save_run("ask", record)
    print(f"Saved: {path.relative_to(config.ROOT)}")


# ---------- chat: personal assistant with memory of this conversation ----------

# Messages about the assistant itself, or edits to its previous reply, never need a notes lookup.
# v2 (after offline run 1): added edit requests such as "all three steps" and "in one sentence",
# which had pulled unrelated notes and derailed the follow up.
CONVERSATIONAL = re.compile(
    r"what can (you|we) do|what can you help|who are you|how do you work|"
    r"make (that|it) (shorter|longer|simpler)|shorten|rewrite|rephrase|more concise|"
    r"another version|in one (sentence|line)|in (two|three|\d) (sentences|bullets|lines)|"
    r"all (three|of them|the steps)|as bullets|simpler|^(hi|hello|hey|thanks|thank you)\b", re.I)

# v3: capability questions get the real capability list attached by the harness
CAPABILITY = re.compile(r"what can (you|we) do|what can you help|who are you|how do you work", re.I)

CHAT_HELP = """Commands:
  /notes <topic>  force a lookup in my wiki for this message
  /reset          forget the conversation so far
  /help           show this help
  /exit           save the transcript and quit"""


def decide_retrieval(message, index):
    """The harness, not the model, decides whether this turn needs my notes."""
    if message.startswith("/notes"):
        query = message[len("/notes"):].strip()
        return query, "forced by /notes"
    if CONVERSATIONAL.search(message):
        return None, "skipped: conversational request"
    top = index.search(message, k=1, kind="source")
    if top and top[0]["score"] >= config.CHAT_RETRIEVE_MIN_SCORE:
        return message, f"used: best match score {top[0]['score']}"
    best = top[0]["score"] if top else 0
    return None, f"skipped: best match score {best} below {config.CHAT_RETRIEVE_MIN_SCORE}"


def run_chat():
    index = load_index()
    print(f"Loading {config.MODEL_ID} (local)...")
    gemma = LocalGemma()
    print(f"Personal wiki assistant. Model: {config.MODEL_ID}, execution: local.")
    print(CHAT_HELP)
    history, turns = [], []
    try:
        while True:
            try:
                message = input("\nyou> ").strip()
            except EOFError:
                break
            if not message:
                continue
            if message in ("/exit", "/quit"):
                break
            if message == "/help":
                print(CHAT_HELP)
                continue
            if message == "/reset":
                history.clear()
                print("Conversation cleared.")
                continue

            query, reason = decide_retrieval(message, index)
            passages = index.search(query, k=config.CHAT_TOP_K, kind="source") if query else []
            text = message[len("/notes"):].strip() if message.startswith("/notes") else message
            reply = gemma.generate(chat_messages(history, text, passages, bool(CAPABILITY.search(text))),
                                   config.CHAT_MAX_TOKENS, config.CHAT_TEMPERATURE)
            citations = check_citations(reply, passages) if passages else None

            print(f"\n[retrieval {reason}]")
            if passages:
                for i, p in enumerate(passages, 1):
                    print(f"  [S{i}] {p['path']} > {p['heading']}")
            print(f"\nassistant> {reply}")
            if citations:
                print(f"[citation check: {citations['status']}]")

            # History keeps the plain messages, not the retrieved passages, to save context
            history += [{"role": "user", "content": text}, {"role": "assistant", "content": reply}]
            history = history[-2 * config.CHAT_HISTORY_TURNS:]
            turns.append({"user": message, "retrieval": reason, "passages": passages,
                          "reply": reply, "citations": citations, "stats": gemma.last})
    except KeyboardInterrupt:
        print()
    if turns:
        path = save_run("chat", {**run_header("chat"), "turns": turns})
        print(f"Transcript saved: {path.relative_to(config.ROOT)}")
