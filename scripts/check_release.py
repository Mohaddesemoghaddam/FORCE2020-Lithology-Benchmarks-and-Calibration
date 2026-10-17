#!/usr/bin/env python3
"""Read-only checks for this public repo; no notebook execution and no third-party packages."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
expected = [
    "02A_FORCE_legacy_RF_exact_reproduction.ipynb",
    "02B_FORCE_legacy_RF_grouped_well_CV.ipynb",
    "02_FORCE_RF_primary_CatBoost_grouped_cv_FIXED.ipynb",
]
errors = []
for file_name in expected:
    path = ROOT / "notebooks" / file_name
    if not path.is_file():
        errors.append(f"Missing notebook: {path}")
        continue
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f"Invalid notebook {path}: {e}")
        continue
    code = "\n".join("".join(c.get("source", [])) for c in doc.get("cells", []) if c.get("cell_type") == "code")
    if "REPO_ROOT" not in code:
        errors.append(f"No portable repository paths in {file_name}")
    if re.search(r"/Users/[^/]+/|[A-Za-z]:\\Users\\[^\\]+", json.dumps(doc,ensure_ascii=False)):
        errors.append(f"Personal user path remains in {file_name}")
    outputs = sum(len(c.get("outputs",[])) for c in doc.get("cells", []))
    print(f"{file_name}: {len(doc.get('cells',[]))} cells, {outputs} saved output records, {path.stat().st_size/1024:.0f} KiB")
for path in list((ROOT / "data").rglob("*.csv")) + list((ROOT / "data").rglob("*.parquet")):
    errors.append(f"Unexpected data file in working tree (check before git add): {path}")
if errors:
    print("\nREVIEW REQUIRED:")
    for err in errors: print(" -",err)
    sys.exit(1)
print("\nPASS — notebook structure and basic public-release checks passed.")
print("Before pushing, also review: git status; git diff --cached --name-only")
