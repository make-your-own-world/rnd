# Research attribution

Density-balanced QEM extends established QEM and robust-statistics techniques for a mesh-processing workflow. The underlying ideas were not presented as a new general simplification family. The contribution is their measured application to nonuniform scanned and composite geometry, the weighting design, and the documented limits that led to depth-guided work.

## Foundations and implementations

- Michael Garland and Paul S. Heckbert, [Surface Simplification Using Quadric Error Metrics](https://publications.ri.cmu.edu/surface-simplification-using-quadric-error-metrics), SIGGRAPH 1997.
- Michael Garland and Paul S. Heckbert, [Simplifying Surfaces with Color and Texture using Quadric Error Metrics](https://www.mgarland.org/research/quadrics.html), IEEE Visualization 1998.
- Carlos DeCoro and Peter Lindstrom, [Real-time Mesh Simplification Using the GPU](https://gfx.cs.princeton.edu/gfx/pubs/DeCoro_2007_RMS/real_time_simplification.pdf), I3D 2007.
- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory*, second edition, Wiley, 2006.
- [Fast Quadric Mesh Simplification](https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification), MIT, and [fast-simplification](https://github.com/pyvista/fast-simplification), MIT.
- [Visualization Toolkit](https://github.com/Kitware/VTK), BSD-style license.
- [NumPy](https://github.com/numpy/numpy), BSD-3-Clause, and [SciPy](https://github.com/scipy/scipy), BSD-3-Clause.

## Design boundary

Robust density statistics can reduce the influence of locally redundant samples, but density is not a complete surface model. It cannot reconstruct layer identity or connectivity destroyed by voxel clustering, and it cannot by itself distinguish useful fine detail from acquisition noise. Those findings motivated the separate depth-guided method and the later combined method.
