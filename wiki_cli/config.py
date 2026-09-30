"""Central settings: folder paths, model identity and tuning knobs, all in one place."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The Obsidian vault: unchanged originals, generated notes, and the landing page
VAULT = ROOT / "vault"
RAW_DIR = VAULT / "raw"
WIKI_DIR = VAULT / "wiki"
INDEX_MD = VAULT / "index.md"

# Machine files live outside the vault so Obsidian never shows them
DATA_DIR = ROOT / "data"
CHUNKS_FILE = DATA_DIR / "chunks.json"        # the retrieval index
MANIFEST_FILE = DATA_DIR / "manifest.json"    # which source produced which notes

CATALOG_FILE = ROOT / "config" / "sources.json"   # source IDs, topic folders, note names
INSTRUCTIONS_DIR = ROOT / "instructions"          # persona and research rules the harness loads
EVIDENCE_DIR = ROOT / "evidence" / "runs"         # every run is saved here

# Local model
MODEL_ID = "mlx-community/gemma-4-e2b-it-4bit"
RUNTIME = "MLX (mlx-lm)"

# Retrieval settings
CHUNK_WORDS = 220             # max words per retrieval passage
ASK_TOP_K = 5                 # passages sent to Gemma in ask mode
CHAT_TOP_K = 3                # passages sent to Gemma when chat decides to look up notes
ASK_MIN_SCORE = 2.0           # ask reports insufficient evidence without calling Gemma below this score
CHAT_RETRIEVE_MIN_SCORE = 5.0 # chat only looks up notes when the best match is at least this strong

# Conversation and generation settings
CHAT_HISTORY_TURNS = 6        # user and assistant pairs kept as chat context
ASK_MAX_TOKENS = 350
CHAT_MAX_TOKENS = 500
INGEST_MAX_TOKENS = 450
ASK_TEMPERATURE = 0.1         # low: factual answers should not vary
CHAT_TEMPERATURE = 0.4        # v3: lowered from 0.7 after runs 1 and 2, the model ignored rules too often
INGEST_TEMPERATURE = 0.2
