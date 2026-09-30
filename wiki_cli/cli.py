"""Command line entry point: parse the command, pick the mode, report useful errors."""
import argparse
import sys
from pathlib import Path

from . import config

DESCRIPTION = f"""Personal wiki CLI: my own notes, a local Gemma model, and keyword retrieval.
Model: {config.MODEL_ID} via {config.RUNTIME}. Execution: local (default and only mode).

Commands:
  ingest PATH        read sources in vault/raw, draft linked wiki notes, rebuild index.md and the search index
  search QUERY       show original matching passages and their paths; no model involved
  ask QUESTION       standalone factual answer from retrieved evidence, with citations,
                     or an explicit insufficient evidence answer; ignores chat history
  chat               personal assistant; remembers this conversation, looks up notes only when useful
  doctor             check device, model cache, index and network status
  help               show this help

Folders: vault/raw (unchanged originals), vault/wiki (generated notes), vault/index.md,
instructions/ (persona and research rules), config/sources.json (source catalog),
data/ (retrieval index), evidence/runs/ (saved outputs of every run)."""


def build_parser():
    parser = argparse.ArgumentParser(prog="wiki", description=DESCRIPTION,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("ingest", help="ingest sources from vault/raw")
    p.add_argument("path", type=Path, help="a folder (usually vault/raw) or one .md file inside it")
    p.add_argument("--force", action="store_true", help="regenerate notes even if the source is unchanged")

    p = sub.add_parser("search", help="show matching original passages")
    p.add_argument("query")
    p.add_argument("-k", type=int, default=5, help="number of passages (default 5)")
    p.add_argument("--include-wiki", action="store_true", help="also search generated wiki notes")

    for name, text in (("ask", "standalone cited answer"), ("chat", "personal assistant")):
        p = sub.add_parser(name, help=text)
        if name == "ask":
            p.add_argument("question")
            p.add_argument("-k", type=int, default=config.ASK_TOP_K, help="passages sent to Gemma")
        p.add_argument("--mode", choices=["local", "online"], default="local",
                       help="where the model runs (only local is implemented)")

    sub.add_parser("doctor", help="check setup")
    sub.add_parser("help", help="show this help")
    return parser


def doctor():
    from .evidence import device_info, network_status
    print(f"Device: {device_info()}")
    print(f"Network: {network_status()}")
    print(f"Index: {'found' if config.CHUNKS_FILE.exists() else 'missing, run: wiki ingest vault/raw'}")
    print(f"Loading {config.MODEL_ID} from local cache...")
    from .model import LocalGemma
    gemma = LocalGemma()
    raw = gemma.generate([{"role": "user", "content": "Reply with one short sentence: what is a wiki?"}],
                         80, 0.1, raw=True)
    print(f"Model loaded in {gemma.load_seconds} s. Raw test output:\n{raw}\n")
    print(f"Measurements: {gemma.last}")


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command in (None, "help"):
        parser.print_help()
        return
    if getattr(args, "mode", "local") == "online":
        sys.exit("Online mode is not implemented in this project. Local is the default: omit --mode or use --mode local.")

    from .model import ModelUnavailable
    try:
        if args.command == "ingest":
            from .ingest import run_ingest
            run_ingest(args.path, force=args.force)
        elif args.command == "search":
            from .modes import run_search
            run_search(args.query, args.k, args.include_wiki)
        elif args.command == "ask":
            from .modes import run_ask
            run_ask(args.question, args.k)
        elif args.command == "chat":
            from .modes import run_chat
            run_chat()
        elif args.command == "doctor":
            doctor()
    except (FileNotFoundError, ValueError, ModelUnavailable) as err:
        sys.exit(f"Error: {err}")
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()
