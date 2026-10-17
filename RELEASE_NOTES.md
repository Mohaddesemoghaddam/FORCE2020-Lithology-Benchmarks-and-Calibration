# Release notes — public repository preparation

- Included three notebooks: the original legacy RF exact reproduction, the original grouped-well legacy RF cross-validation, and the FIXED RF/CatBoost comparator.
- Excluded the superseded original non-FIXED comparator and the unrelated GEOLINK LAS audit.
- Adapted ONLY project path configuration, to use `FORCE_REPO_ROOT`, `FORCE_DATA_DIR`, `FORCE_PREPARED_DIR` and `FORCE_RESULTS_DIR`. This changes input/output locations, **not model methods**.
- Saved outputs in 02A and 02B are from their earlier executions and were preserved; historical private local user paths in displayed outputs were redacted. No notebook was re-run.
- Added `os` import to FIXED notebook to support the environment-based path configuration.
- Added a brief release-note Markdown paragraph to each notebook and release metadata; these are documentary changes, not scientific-code changes.
- The dataset, preprocessed artifacts, models, full output reports, and GEOLINK files are absent.
