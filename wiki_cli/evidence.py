"""Save every run as a readable Markdown card plus one JSON line, and record the environment."""
import json
import platform
import socket
import subprocess
from datetime import datetime

from . import config


def network_status():
    """Proof for the offline demo: can this machine open any internet connection right now?"""
    try:
        socket.create_connection(("1.1.1.1", 443), timeout=1.5).close()
        return "online"
    except OSError:
        return "offline (no internet connection)"


def device_info():
    info = {"os": platform.platform(), "machine": platform.machine(), "python": platform.python_version()}
    if platform.system() == "Darwin":
        info["os"] = f"macOS {platform.mac_ver()[0]}"
        try:
            sysctl = lambda key: subprocess.run(["sysctl", "-n", key], capture_output=True, text=True).stdout.strip()
            info["chip"] = sysctl("machdep.cpu.brand_string")
            info["unified_memory_gb"] = round(int(sysctl("hw.memsize")) / 2**30)
        except Exception:
            pass
    return info


def run_header(mode):
    try:
        from importlib.metadata import version
        runtime_version = f"mlx-lm {version('mlx-lm')}, mlx {version('mlx')}"
    except Exception:
        runtime_version = "unknown"
    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "mode": mode,
        "execution": "local",
        "model": config.MODEL_ID,
        "runtime": f"{config.RUNTIME}: {runtime_version}",
        "network": network_status(),
        "device": device_info(),
    }


def save_run(mode, record):
    config.EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = config.EVIDENCE_DIR / f"{stamp}-{mode}.md"
    path.write_text(render(record), encoding="utf-8")
    with open(config.EVIDENCE_DIR / "runs.jsonl", "a", encoding="utf-8") as log:
        log.write(json.dumps(record) + "\n")
    return path


def render_passages(passages):
    lines = []
    for i, p in enumerate(passages, 1):
        lines += [f"**[S{i}]** `{p['path']}` > {p['heading']} (score {p.get('score')})", "",
                  "> " + p["text"].replace("\n", "\n> "), ""]
    return lines


def render(record):
    lines = [f"# {record['mode'].title()} run, {record['timestamp']}", ""]
    for key in ("execution", "model", "runtime", "network"):
        lines.append(f"* **{key}:** {record[key]}")
    lines.append(f"* **device:** {record['device']}")
    if record.get("stats"):
        lines.append(f"* **measurements:** {record['stats']}")
    lines.append("")
    if record["mode"] == "chat":
        for turn in record["turns"]:
            lines += [f"**You:** {turn['user']}", "",
                      f"*Retrieval: {turn['retrieval']}*", ""]
            if turn["passages"]:
                lines += render_passages(turn["passages"])
            lines += [f"**Assistant:** {turn['reply']}", ""]
            if turn.get("citations"):
                lines += [f"*Citation check: {turn['citations']['status']}*", ""]
        return "\n".join(lines)
    if record.get("query"):
        lines += [f"## {'Question' if record['mode'] == 'ask' else 'Query'}", "", record["query"], ""]
    if "passages" in record:
        lines += ["## Retrieved passages", ""] + render_passages(record["passages"])
    if record.get("answer"):
        lines += ["## Answer", "", record["answer"], ""]
    if record.get("citations"):
        c = record["citations"]
        lines += ["## Citation check", "", f"Status: {c['status']}", ""]
        lines += [f"* {x['label']} = `{x['path']}` > {x['heading']}" for x in c["cited"]]
        if c["invalid"]:
            lines.append(f"* Invalid labels: {', '.join(c['invalid'])}")
        lines.append("")
    if record.get("details"):
        lines += ["## Details", "", "```", json.dumps(record["details"], indent=2), "```", ""]
    return "\n".join(lines)
