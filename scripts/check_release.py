#!/usr/bin/env python3
"""Lightweight static checks for this research release; no notebook execution."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    "02A_FORCE_legacy_RF_exact_reproduction.ipynb",
    "02B_FORCE_legacy_RF_grouped_well_CV.ipynb",
    "03_FORCE_nested_grouped_temperature_calibration_CORRECTED.ipynb",
    "02_FORCE_RF_primary_CatBoost_grouped_cv_FIXED.ipynb",
]
issues = []
for name in EXPECTED:
    path = ROOT / "notebooks" / name
    if not path.is_file():
        issues.append(f"Missing notebook: {name}")
        continue
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        issues.append(f"Unreadable notebook {name}: {exc}")
        continue
    code = "\n".join("".join(cell.get("source", [])) for cell in doc.get("cells", []) if cell.get("cell_type") == "code")
    if "REPO_ROOT" not in code or "FORCE_RESULTS_DIR" not in code:
        issues.append(f"Portable paths not detected in {name}")
    if re.search(r"/Users/[^/]+/|[A-Za-z]:\\Users\\[^\\]+", json.dumps(doc, ensure_ascii=False)):
        issues.append(f"Personal filesystem path found in {name}")
    if re.search(r"(?:AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,})", json.dumps(doc)):
        issues.append(f"Possible embedded token in {name} — inspect manually")
    outputs = sum(len(cell.get("outputs", [])) for cell in doc.get("cells", []))
    print(f"{name}: {len(doc.get('cells', []))} cells, {outputs} stored outputs, {path.stat().st_size / 1024:.1f} KiB")
for bad in list((ROOT / 'data').rglob('*.csv')) + list((ROOT / 'data').rglob('*.parquet')):
    issues.append(f"Local dataset in tree (check gitignore/staging): {bad}")
if issues:
    print("\nPlease review:")
    for issue in issues:
        print(' -', issue)
    sys.exit(1)
print("\nPASS: required notebooks and basic release checks succeeded.")
print("Before pushing, inspect `git diff --cached --name-only` for unintended files.")
