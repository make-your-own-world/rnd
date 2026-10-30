# Independent research and attribution

This report documents experiments, implementation choices, measurements, and interpretations so others can inspect, reproduce, and build on the work. Established methods and incorporated software are credited below. Related work may be independently rediscovered or become known later; references can be corrected as additional information becomes available. The purpose is to preserve and share useful knowledge, including the decisions and unsuccessful approaches that led to the result.

- [VTK Flying Edges](https://vtk.org/doc/nightly/html/classvtkFlyingEdges3D.html): Incorporated sampled isosurface extraction; credited algorithm by Schroeder, Maynard and Geveci.
- [VTK hull and morphology](https://vtk.org/): Incorporated enclosing priors and image operations.
- [Surface-preserving completion](../solid-completion/paper.md): Companion account of constrained volume preparation, measured-facet retention, and boundary repair.

The source snapshots retain the application source license. Third-party libraries retain their own licenses and notices in the MeshMill distribution. No third-party binaries are included here.
