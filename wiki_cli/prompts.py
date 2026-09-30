"""Load the instruction files and assemble the exact messages each mode sends to Gemma."""
from . import config


def load_instruction(name):
    return (config.INSTRUCTIONS_DIR / name).read_text(encoding="utf-8")


def format_passages(passages):
    """Label each passage [S1], [S2]... with its file and section so Gemma can cite it."""
    return "\n\n".join(f"[S{i}] {p['path']} > {p['heading']}\n{p['text']}"
                       for i, p in enumerate(passages, 1))


def ask_messages(question, passages):
    """Ask mode: research rules plus retrieved evidence. No persona, no chat history.
    v3: the question and the key reminders come last, where a small model attends most."""
    user = (f"Retrieved passages:\n\n{format_passages(passages)}\n\n"
            f"Question: {question}\n\n"
            "Answer using only these passages. If the question has several parts, answer every part, "
            "each with its own [S#] citation. If the passages do not answer it, start with "
            "\"Insufficient evidence:\".")
    return [{"role": "system", "content": load_instruction("wiki-instructions.md")},
            {"role": "user", "content": user}]


def chat_messages(history, message, passages, capability_question=False):
    """Chat mode: persona, recent conversation, and notes only when the harness retrieved them.
    v3: the harness appends reminders at the end of the message instead of relying on the persona alone."""
    content = message
    if capability_question:
        content += "\n\n" + load_instruction("capabilities.md")
    if passages:
        content += ("\n\nNotes retrieved from my wiki for this message:\n\n" + format_passages(passages) +
                    "\n\nReminder: cite every fact you take from these notes as [S1], [S2]. "
                    "If anything I said contradicts the notes, point it out and cite the note.")
    return [{"role": "system", "content": load_instruction("persona.md")},
            *history,
            {"role": "user", "content": content}]


def note_messages(title, source_text):
    """Ingest: turn one section of a source into a wiki note summary."""
    user = f"Note title: {title}\n\nSource text:\n{source_text}\n\nWrite the SUMMARY and KEY POINTS now."
    return [{"role": "system", "content": load_instruction("ingest-instructions.md")},
            {"role": "user", "content": user}]


def link_messages(title, summary, candidates):
    """Ingest: choose related notes from a fixed list of existing titles."""
    listing = "\n".join(f"- {t}" for t in candidates)
    user = f"Note: {title}\nSummary: {summary}\n\nCandidate notes:\n{listing}\n\nPick up to 3."
    return [{"role": "system", "content": load_instruction("linking-instructions.md")},
            {"role": "user", "content": user}]
