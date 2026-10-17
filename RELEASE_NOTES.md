# Release notes — baseline and calibration integration

## Updated scope

The former `FORCE2020-Lithology-Baselines` repository is now documented as `FORCE2020-Lithology-Benchmarks-and-Calibration`, because its pipeline includes a full nested probability-calibration stage beyond classifier baselines. **Rename the already published GitHub repository rather than creating a second copy, preserving commit history.**

## Included notebooks

- `02A_FORCE_legacy_RF_exact_reproduction.ipynb` — reproduction of the legacy RF model (saved execution).
- `02B_FORCE_legacy_RF_grouped_well_CV.ipynb` — well-held-out 5-fold evaluation (saved execution).
- `03_FORCE_nested_grouped_temperature_calibration_CORRECTED.ipynb` — corrected nested temperature scaling (saved full execution).
- `02_FORCE_RF_primary_CatBoost_grouped_cv_FIXED.ipynb` — comparator implementation (not yet run in supplied notebook).

The superseded uncorrected comparison and calibration notebooks are intentionally **not** included. GEOLINK is excluded.

## File changes and honesty about verification

- The prior 02A, 02B, and RF/CatBoost notebooks were copied **unchanged from the prior public-release ZIP**.
- The corrected 03 notebook was copied from the uploaded original, with only portable path configuration, `import os`, correction of an obsolete Markdown path and a short provenance note. Math, preprocessing, nested split logic, hyperparameters, caching and metric calculations were **not** modified.
- The corrected 03 notebook **retains its previous saved outputs**, including its last pooled results and reliability diagram. A private historical filesystem prefix in recorded outputs was redacted. The notebook was **not** re-executed after the portability update.
- No raw FORCE data, preprocessed artifacts, model weights, generated predictions or cache files are included.
- README, dependency information and public-release checks were updated. Full execution requires the input data and artifacts documented in README.
