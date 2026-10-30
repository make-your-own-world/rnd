# Experiments and reproduction

The recorded tables come from generated bracket and tube fixtures. Their reference, incomplete, and completed meshes are included in `data`. Geometry screenshots illustrate the separate scan workflows and are not the inputs to those numerical tables.

## Reproduce

Use the MeshMill 0.4 source checkout and its declared dependencies. From this paper directory:

```powershell
python experiments/code/reproduce_completion_and_cast.py --source <MeshMill-checkout> --output <new-result-directory>
```

The runner generates the fixtures and measures retained triangles, open edges, volume, and construction time. It also measures split versus unsplit material volume. New results go to a new directory, preserving the recorded evidence. Construction timings exclude application launch and downstream reduction. Both papers use the same fixture run so their completion and cavity stages can be examined together.

`data/source-manifest.json` identifies the included source snapshots. The snapshots support inspection; the full checkout supplies cross-module imports. `data/clearance-measurements.json`, when present, records six explicitly named face-normal rays per outer shape, measured on the saved geometry. The paper identifies these as sampled measurements rather than a uniform offset.

## Geometry evidence

`data/*.vtp` contains the actual fixture surfaces used for plots and volume checks. The scan and downstream screenshots contain geometry only. Their figure captions identify what each view demonstrates.
