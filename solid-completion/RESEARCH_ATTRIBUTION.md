# Independent research and attribution

This report documents experiments, implementation choices, measurements, and interpretations so others can inspect, reproduce, and build on the work. Established methods and incorporated software are credited below. Related work may be independently rediscovered or become known later; references can be corrected as additional information becomes available. The purpose is to preserve and share useful knowledge, including the decisions and unsuccessful approaches that led to the result.

- [TetGen](https://wias-berlin.de/software/tetgen/): Incorporated constrained tetrahedralization.
- [Boykov and Kolmogorov, min-cut/max-flow comparison](https://discovery.ucl.ac.uk/id/eprint/13383/): Upstream MAXFLOW citation; PyMaxflow supplies the cut implementation.
- [Python-SAT and RC2](https://github.com/pysathq/pysat): Incorporated SAT/MaxSAT infrastructure.
- [MeshFix and PyMeshFix](https://github.com/pyvista/pymeshfix): Incorporated repair and validation; Attene (2010), A Lightweight Approach to Repairing Digitized Polygon Meshes, is the upstream research citation.
- [Robust Inside-Outside Segmentation using Generalized Winding Numbers](https://users.cs.utah.edu/~ladislav/jacobson13robust/jacobson13robust.html): Related constrained-volume architecture; this implementation does not use its winding-number query.

The source snapshots retain the application source license. Third-party libraries retain their own licenses and notices in the MeshMill distribution. No third-party binaries are included here.
