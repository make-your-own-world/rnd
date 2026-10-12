# Research attribution

This publication builds on public research and open-source implementations used to understand, reproduce, and compare mesh-reduction strategies. Inclusion records influence or evaluation. It does not imply that source code was copied into the combined method.

## Mathematical and algorithmic foundations

- Michael Garland and Paul S. Heckbert, [Surface Simplification Using Quadric Error Metrics](https://publications.ri.cmu.edu/surface-simplification-using-quadric-error-metrics), SIGGRAPH 1997. This supplies the accumulated-plane quadric objective and edge-collapse foundation.
- Michael Garland and Paul S. Heckbert, [Simplifying Surfaces with Color and Texture using Quadric Error Metrics](https://www.mgarland.org/research/quadrics.html), IEEE Visualization 1998. This informs attribute-aware quadric weighting.
- Carlos DeCoro and Peter Lindstrom, [Real-time Mesh Simplification Using the GPU](https://gfx.cs.princeton.edu/gfx/pubs/DeCoro_2007_RMS/real_time_simplification.pdf), I3D 2007. This motivated the measured voxel and GPU-clustering comparison.
- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory*, second edition, Wiley, 2006. The data-processing inequality is used to explain why a many-to-one voxel map cannot restore discarded within-cell surface identity.

## Open-source implementations and computing stack

- [Fast Quadric Mesh Simplification](https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification), MIT, and [fast-simplification](https://github.com/pyvista/fast-simplification), MIT, supply the production QEM baseline and finishing stage.
- [Visualization Toolkit](https://github.com/Kitware/VTK), BSD-style license, supplies mesh I/O, inspection, and comparison reducers.
- [RXMesh](https://github.com/owensgroup/RXMesh), BSD-2-Clause, was evaluated as a public GPU-resident dynamic-mesh reference. Its code is not incorporated.
- [CuPy](https://github.com/cupy/cupy), MIT, supplies GPU array execution for depth and density analysis.
- [NumPy](https://github.com/numpy/numpy), BSD-3-Clause, and [SciPy](https://github.com/scipy/scipy), BSD-3-Clause, supply numerical, spatial, and validation operations.

## Contribution of this work

The combined method fuses adaptive depth-gauge surface evidence with robust local density weighting, then uses a boundary-aware global QEM pass for topology reduction. It preserves the original indexed mesh until the ordered reducer has the evidence needed to decide which geometry is redundant. The retained GPU voxel experiment is a comparison path, not a preprocessing stage, because voxel clustering irreversibly merges distinct samples that share a cell.
