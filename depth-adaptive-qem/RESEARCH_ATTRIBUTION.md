# Research attribution

This record identifies the public research and open-source projects consulted during the development
and evaluation of Depth Adaptive QEM. Inclusion means that a source helped explain the problem,
supplied a comparison method, or provided an implementation used in an experiment. It does not mean
that its source code was copied into the Depth Adaptive QEM implementation.

Commercial, closed-source, paywalled, and account-gated products are intentionally omitted. The list
is divided by how each source was used so that conceptual influence is not confused with a software
dependency.

## Public research

1. Michael Garland and Paul S. Heckbert, [Surface Simplification Using Quadric Error
   Metrics](https://publications.ri.cmu.edu/surface-simplification-using-quadric-error-metrics),
   SIGGRAPH 1997. This is the mathematical foundation for accumulated plane quadrics and ranked edge
   collapse. Depth Adaptive QEM retains QEM for final topology reduction while changing the surface
   evidence presented to that reducer.

2. William J. Schroeder, Jonathan A. Zarge, and William E. Lorensen, [Decimation of Triangle
   Meshes](https://doi.org/10.1145/133994.134010), SIGGRAPH 1992. This work supplied the
   topology-oriented vertex-removal baseline represented in the experiments by VTK's
   `vtkDecimatePro`.

3. Christopher DeCoro and Peter Lindstrom, [Real-time Mesh Simplification Using the
   GPU](https://gfx.cs.princeton.edu/gfx/pubs/DeCoro_2007_RMS/real_time_simplification.pdf),
   I3D 2007. Its streaming quadric-clustering formulation motivated the tested GPU clustering path
   and clarified the speed-versus-global-order tradeoff. The published method was reproduced for
   evaluation; its source code was not incorporated.

4. Mohamed H. Mousa and Mohamed K. Hussein, [High-performance simplification of triangular surfaces
   using a GPU](https://doi.org/10.1371/journal.pone.0255832), PLOS ONE 2021. Its conflict-set and
   independent-collapse treatment informed the parallel-collapse prototypes and their topology
   checks. The experiments showed that conservative independent sets were valid but too small on the
   retained layered scan, while relaxed sets changed topology or stalled above target.

## Open-source projects evaluated or reviewed

1. [RXMesh](https://github.com/owensgroup/RXMesh), BSD-2-Clause. RXMesh demonstrates GPU-resident
   dynamic triangle-mesh processing and includes a QSlim example. It was built and timed against the
   retained fixture. Its code was not incorporated into MeshMill. The measured conversion and
   reduction behavior is recorded in the experiment reports.

2. [Microsoft TRELLIS](https://github.com/microsoft/TRELLIS), MIT, and
   [trellis.cpp](https://github.com/pwilkin/trellis.cpp), MIT. These projects were reviewed as public
   GPU-oriented geometry and structured-representation references. Their image-to-3D generation goal
   differs from deterministic reduction of an existing indexed mesh. Neither codebase was
   incorporated into Depth Adaptive QEM.

3. [Fast Quadric Mesh Simplification](https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification),
   MIT. This implementation supplied the practical threshold-scheduled QEM baseline used to
   understand why a global compiled reducer remained difficult to outperform with GPU mutation
   prototypes.

4. [fast-simplification](https://github.com/pyvista/fast-simplification), MIT. These Python bindings
   wrap Fast Quadric Mesh Simplification. MeshMill uses this package for Fast QEM and for the final
   boundary-preserving topology reduction stage of Depth Adaptive QEM. This is an incorporated
   open-source dependency, not merely a research reference.

5. [Visualization Toolkit (VTK)](https://github.com/Kitware/VTK), BSD-style open-source license.
   MeshMill uses VTK for mesh I/O, display, selection support, and the `vtkQuadricDecimation` and
   `vtkDecimatePro` comparison paths. The corresponding public references are the
   [`vtkQuadricDecimation` documentation](https://vtk.org/doc/nightly/html/classvtkQuadricDecimation.html),
   [`vtkQuadricDecimation` source](https://github.com/Kitware/VTK/blob/master/Filters/Core/vtkQuadricDecimation.cxx),
   and [`vtkDecimatePro` documentation](https://vtk.org/doc/nightly/html/classvtkDecimatePro.html).

## Open-source experimental computing stack

The retained reproduction programs use the following public projects. They provide numerical and GPU
execution facilities rather than the Depth Adaptive QEM method itself.

- [CuPy](https://github.com/cupy/cupy), MIT: GPU arrays, kernels, reductions, sorting, filtering, and
  synchronization used by the surface-analysis and mutation prototypes.
- [NumPy](https://github.com/numpy/numpy), BSD-3-Clause: host-side array representation, statistics,
  indexing, and report preparation.
- [SciPy](https://github.com/scipy/scipy), BSD-3-Clause: sparse connectivity, connected components,
  spatial search, and triangulation used in selected prototypes and validation paths.

## What is original to this work

The physical depth-gauge model, adaptive probe radius and spacing, multi-directional surface support,
confidence-limited displacement, unsupported-region preservation, and the decision to feed that
surface measurement into a proven global QEM reducer were developed within the MeshMill work. The
public sources above supplied mathematical foundations, comparison implementations, GPU data-structure
examples, and failed or incomplete alternative paths. They did not supply the combined Depth Adaptive
QEM design.

The project reports measured outcomes for the retained fixture rather than claiming that an evaluated
project is generally slow, inaccurate, or unsuitable. Different inputs, hardware, integration choices,
and project objectives can produce different results.
