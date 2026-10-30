# Closing Incomplete Meshes Without Replacing Their Measured Surface

Version 1.0.

MeshMill completes missing scan surfaces by preserving measured triangles and constructing the missing boundary around them. The method divides the surrounding space into tetrahedra, labels material using oriented surface evidence, and repairs the resulting boundary locally. A concave bracket and a hollow tube demonstrate the result: the missing patches close, every input facet is retained, and the notch and through-hole remain empty. This paper explains the mathematics, implementation choices, and experiments behind that result.

- [Paper](paper.md)
- [PDF](solid-completion-v1.0.pdf)
- [Experiments and reproduction](EXPERIMENT_CATALOG.md)
- [Recorded results](data/results.csv)
- [Attribution](RESEARCH_ATTRIBUTION.md)
