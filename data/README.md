# Local data (not committed)

- Place FORCE 2020 `train.csv` and `test.csv` in `data/raw/`.
- Place preprocessing-stage artifacts in `data/prepared/`:
  - `10_grouped_5fold_well_assignment.csv` (required by 02B unless cleaned Parquet supplies `WELL`, `GROUP_FOLD`)
  - `FORCE_train_cleaned_with_splits.parquet` (required by RF/CatBoost benchmark)
  - `07_causal_project_contract_v0_2_1.json` (required by RF/CatBoost benchmark)

These files are not included in the GitHub repository. See the main README for their provenance and the required schema.
