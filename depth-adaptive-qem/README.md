# Depth Adaptive QEM

Depth Adaptive QEM is a geometry-reduction method developed for large, open, layered scan meshes.
It uses adaptive GPU surface measurements to suppress supported scan-scale variation, then delegates
final topology reduction to a boundary-preserving global quadric-error reducer.

- [Read the paper](paper.md)
- [Download the rendered paper](depth-adaptive-qem-v1.1.pdf)
- [Review the complete public research and open-source attribution](RESEARCH_ATTRIBUTION.md)
- [Inspect the normalized benchmark observations](data/quality-observations.csv)

Version 1.1 documents the method, mathematical derivation, controlled comparison, unsuccessful
alternative strategies, performance split, limitations, and relationship to prior public work.

The publication set contains only the paper, rendered PDF, citation metadata, attribution record,
figures referenced by the paper, and the normalized measurements supporting its comparison tables.
Local build tools, working notes, raw run archives, generated meshes, machine details, paths, caches,
and development history are excluded.

## Scope

The retained benchmark uses one large composite scan fixture. Its results establish behavior on that
fixture rather than universal superiority across arbitrary meshes. Additional independent fixtures
and reproduction remain useful follow-up work.

## Citation

Citation metadata is available in [CITATION.cff](CITATION.cff).

## License

Repository licensing is provided at the repository root. Referenced publications and open-source
projects retain their respective copyrights and licenses.
