#!/usr/bin/env python3
"""Build the static gallery manifest from Git history; newest added photos first."""
import json
import pathlib
import subprocess
from datetime import datetime, timezone

root = pathlib.Path(__file__).resolve().parents[1]
directory = root / "public" / "past-jobs-photos"
output = root / "public" / "past-jobs-gallery.json"
extensions = {".jpg", ".jpeg", ".png", ".webp", ".avif", ".gif"}
entries = []
for file in directory.iterdir():
    if not file.is_file() or file.suffix.lower() not in extensions:
        continue
    relative = file.relative_to(root).as_posix()
    result = subprocess.run(
        ["git", "log", "--follow", "--diff-filter=A", "--format=%aI", "--", relative],
        cwd=root, capture_output=True, text=True, check=True)
    dates = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    # Earliest addition commit, not last edit, so changing an image doesn't reorder it.
    added = dates[-1] if dates else datetime.now(timezone.utc).isoformat()
    name = file.stem.replace("_", " ").replace("-", " ").strip()
    entries.append({
        "src": "/past-jobs-photos/" + file.name,
        "title": name or "Past job",
        "addedAt": added,
    })
entries.sort(key=lambda entry: (entry["addedAt"], entry["src"]), reverse=True)
output.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Generated {len(entries)} gallery images.")
