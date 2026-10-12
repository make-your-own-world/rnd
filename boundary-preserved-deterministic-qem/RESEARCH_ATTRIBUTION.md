# Research and implementation attribution

Boundary-Preserved Deterministic QEM combines established ideas into a tested MeshMill production
pipeline. The name describes verified behavior and is not a claim that every component is novel.

## Foundational work

- Michael Garland and Paul Heckbert, *Surface Simplification Using Quadric Error Metrics*,
  SIGGRAPH 1997. This establishes accumulated quadric error and iterative contraction.
- Peter Lindstrom, *Out-of-Core Simplification of Large Polygonal Models*, SIGGRAPH 2000. This
  establishes a major out-of-core simplification reference and discusses bounded memory.
- Paolo Cignoni and colleagues, *External Memory Management and Simplification of Huge Meshes*.
  This establishes octree-based external-memory mesh processing and protected block boundaries.

## Project-specific engineering contribution

The project contribution is the integrated contract: deterministic adaptive ownership, exact
largest-remainder target allocation, conservative boundary-coordinate validation, memory-bounded
parallel scheduling, atomic per-tile checkpoints, corruption recovery, deterministic ordered
streaming, cancellation-safe publication, and tests that distinguish simplification reduction from
assembly loss.

No external implementation code is included in the publication package. The reference
implementation is the MeshMill implementation snapshot used for the reported measurements.
