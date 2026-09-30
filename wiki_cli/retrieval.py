"""The retrieval tool: a keyword (BM25) index over passages. Needs no model and no network."""
import json
import math
import re
from collections import Counter

from . import config
from .chunking import chunk_markdown

STOPWORDS = set("""a an and are as at be by can do does for from has have how i if in is it its
me my of on or should so that the their them then there these this to was what when where which
who why will with you your""".split())

K1, B = 1.5, 0.75   # standard BM25 constants: term frequency saturation and length normalization


def stem(word):
    """Very light stemming so 'offers' matches 'offer' and 'opens' matches 'open'."""
    for suffix in ("ing", "ed", "es", "s"):
        if len(word) > 4 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def tokenize(text):
    words = re.findall(r"[a-z0-9$%]+(?:\.[0-9]+)?", text.lower())
    return [stem(w) for w in words if w not in STOPWORDS]


class Index:
    def __init__(self, passages):
        self.passages = passages
        self.docs = [tokenize(p["heading"] + " " + p["text"]) for p in passages]
        self.term_counts = [Counter(doc) for doc in self.docs]
        self.avg_len = sum(len(d) for d in self.docs) / max(len(self.docs), 1)
        n = len(self.docs)
        doc_freq = Counter(term for doc in self.docs for term in set(doc))
        # rare words weigh more than common ones (inverse document frequency)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in doc_freq.items()}

    def search(self, query, k=5, kind=None):
        """Return the top k passages by BM25 score. kind='source' limits to raw originals."""
        terms = tokenize(query)
        scored = []
        for i, counts in enumerate(self.term_counts):
            if kind and self.passages[i]["kind"] != kind:
                continue
            length_norm = 1 - B + B * len(self.docs[i]) / self.avg_len
            score = sum(self.idf[t] * counts[t] * (K1 + 1) / (counts[t] + K1 * length_norm)
                        for t in terms if t in counts)
            if score > 0:
                scored.append((score, i))
        scored.sort(reverse=True)
        return [dict(self.passages[i], score=round(s, 2)) for s, i in scored[:k]]


def build_index():
    """Chunk every Markdown file in raw/ and wiki/ and save the passages to data/chunks.json."""
    passages = []
    for kind, folder in (("source", config.RAW_DIR), ("wiki", config.WIKI_DIR)):
        for path in sorted(folder.rglob("*.md")):
            rel = path.relative_to(config.VAULT).as_posix()
            for n, chunk in enumerate(chunk_markdown(path.read_text(encoding="utf-8"), config.CHUNK_WORDS), 1):
                passages.append({"id": f"{rel}#{n}", "kind": kind, "path": rel, **chunk})
    config.DATA_DIR.mkdir(exist_ok=True)
    config.CHUNKS_FILE.write_text(json.dumps(passages, indent=1), encoding="utf-8")
    return passages


def load_index():
    if not config.CHUNKS_FILE.exists():
        raise FileNotFoundError("No retrieval index found. Run: wiki ingest vault/raw")
    return Index(json.loads(config.CHUNKS_FILE.read_text(encoding="utf-8")))
