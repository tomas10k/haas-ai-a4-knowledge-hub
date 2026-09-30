"""Split Markdown into sections (for wiki notes) and passages (for retrieval), keeping locations."""
import re
from dataclasses import dataclass

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


@dataclass
class Section:
    heading: str   # the level 2 heading, for example "7. First offers"
    text: str      # everything under it, including ### subsections


def strip_frontmatter(markdown):
    return FRONTMATTER.sub("", markdown, count=1)


def split_sections(markdown):
    """Return the level 2 sections of a document. Ingest turns each one into a wiki note."""
    sections, heading, lines = [], None, []
    for line in markdown.splitlines():
        match = HEADING.match(line)
        if match and len(match.group(1)) == 2:
            if heading is not None:
                sections.append(Section(heading, "\n".join(lines).strip()))
            heading, lines = match.group(2).strip(), []
        elif heading is not None:
            lines.append(line)
    if heading is not None:
        sections.append(Section(heading, "\n".join(lines).strip()))
    return sections


def chunk_markdown(markdown, max_words):
    """Return retrieval passages as {"heading", "text"} dicts.

    Splits at every heading, then at blank lines, and merges paragraphs under the same
    heading until a passage reaches max_words. Each passage keeps its heading path,
    for example "10. Salary and job offer negotiation", so citations can point to it.
    """
    path = []          # stack of (level, heading text)
    blocks = []        # (heading path, paragraph text)
    paragraph = []

    def flush():
        if paragraph:
            label = " > ".join(title for _, title in path) or "Introduction"
            blocks.append((label, "\n".join(paragraph).strip()))
            paragraph.clear()

    for line in strip_frontmatter(markdown).splitlines():
        match = HEADING.match(line)
        if match:
            flush()
            level = len(match.group(1))
            if level == 1:          # the document title is not a section
                path = []
                continue
            path = [item for item in path if item[0] < level] + [(level, match.group(2).strip())]
        elif not line.strip():
            flush()
        else:
            paragraph.append(line)
    flush()

    passages = []
    for heading, text in blocks:
        previous = passages[-1] if passages else None
        if previous and previous["heading"] == heading and \
                len((previous["text"] + " " + text).split()) <= max_words:
            previous["text"] += "\n\n" + text
        else:
            passages.append({"heading": heading, "text": text})
    return passages
