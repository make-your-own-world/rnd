# Experiments and reproduction

## Recorded evidence

- Nine intentionally misaligned synthetic fixtures in `data/calibration-results.csv`.
- 21 focused passing checks in `data/regression-results.csv`.
- Exact source and test snapshots identified by `data/source-manifest.json`.
- Failure discussions are development observations, not invented comparative benchmarks.

## Run the checks

Use a matching MeshMill 0.4 checkout with its declared test environment. From that checkout:

```powershell
python -m pytest tests/test_axis_datum_stress.py tests/test_axis_datum.py tests/test_lathe_spindle.py tests/test_lathe_contact.py tests/test_orientation_layout.py -q
```

The package snapshots support inspection; the application checkout supplies cross-module dependencies and test configuration. Required numerical components include NumPy and VTK. The fixtures are generated from primitives, with no external scan required.

## Reproduce the numerical fixture run

```powershell
python experiments/code/reproduce_calibration.py --source <MeshMill-checkout> --output <new-result-folder>
```

The runner creates a new output folder and JSON result, including correction histories. It uses independent 257-angle checks and a stable-fit recheck. Keep new timings separate from recorded evidence. Timings exclude viewer startup and animated inspection. Numerical tolerances and backend versions can affect results.
