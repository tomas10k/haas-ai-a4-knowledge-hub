"""Check that an answer's citations point to passages that were actually retrieved."""
import re

INSUFFICIENT = "insufficient evidence"


def cited_labels(answer):
    """Find [S1], [S2, S3] and [S1][S4] style citations; return the numbers."""
    numbers = set()
    for group in re.findall(r"\[(S\d+(?:\s*,\s*S?\d+)*)\]", answer):
        numbers.update(int(n) for n in re.findall(r"\d+", group))
    return sorted(numbers)


def check_citations(answer, passages):
    numbers = cited_labels(answer)
    valid = [n for n in numbers if 1 <= n <= len(passages)]
    invalid = [n for n in numbers if n not in valid]
    declined = INSUFFICIENT in answer.lower()
    if declined and not valid:
        status = "declined: insufficient evidence"
    elif invalid:
        status = "FAIL: cites passages that were not retrieved"
    elif valid:
        status = "ok: every citation points to a retrieved passage"
    else:
        status = "FAIL: answer has no citations"
    return {
        "status": status,
        "cited": [{"label": f"S{n}", "path": passages[n - 1]["path"], "heading": passages[n - 1]["heading"]}
                  for n in valid],
        "invalid": [f"S{n}" for n in invalid],
    }
