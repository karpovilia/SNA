Handling nodes without natural features
- Learnable node features: for 
---
## Deep Graph Library (DGL)
- Started as research project out of NYU Shanghai
- Joined forces with AWS and is now developed/maintained there in collaboration with NVIDIA and the open source community
- Differentiated by speed and scalability
	- Supports multi-GPU and multi-machine with multi-GPU
- Documentation has nice section of tutorials for learning and there are many [examples](https://github.com/dmlc/dgl/tree/master/examples/pytorch) in github
- Backend is framework agnostic
---
## DGL 1.0 release
[dgl blog](https://www.dgl.ai/release/2023/02/20/release.html)
![](https://www.dgl.ai/assets/images/posts/2023-02-20-release/arch.png)

---
## Useful APIs and data structures
- Named node and edge features
	- g.ndata['x']=X
	- g.edata['a']=E
- Graph processing
	- dgl.add_reverse_edges(g)
	- dgl.add_self_loop(g)
- Graph querying
	- g.num_nodes()
	- g.num_edges()
	- g.has_edges_between(u,v)
	- g.in_degrees()
- Message passing APIs
	- $h_u=\frac{1}{N_u}\sum\limits_{V\in N_u}{x_v}$ = g.update_all(fn.copy_u('x', 'm'), fn.mean('m','h'))
- Increasingly supporting heterogeneous graphs

---
## PyTorch Geometric (PyG)
- Built on top of PyTorch
- Developed at TU Dortmund and Stanford Universities
- Overlap with group that runs the Open Graph Benchmark
- Standardizes the API around defining “message” and “update” functions, along with specifying an aggregator
- Has a large set of built-in [datasets](https://pytorch-geometric.readthedocs.io/en/latest/modules/datasets.html) and [implementations](https://github.com/pyg-team/pytorch_geometric/tree/master/benchmark/kernel)

---
## New(er) comers
- Jraph
	- Comes from DeepMind
	- Built on top of JAX
- TensorflowGNNs
	- Alpha release announced Nov 2021
	- Keras-style API
	- A stated emphasis on heterogeneous graphs
---
## Open Graph Benchmark (ogb.stanford.edu)
- Larger and more realistic benchmark graph datasets
	- Node, Link and Graph property prediction tasks
- Wrapped in a Python package for easy loading into PyGand DGL
	- Comes with a pre-defined train/val/test split
- Also comes with built in “Evaluators” for each dataset to ensure performance is consistently measured
- Each dataset has a leaderboard, each row is a method’s performance with paper + code
- There’s also a “Large-Scale” version with much larger graphs

---
## References
- Wang, M., Zheng, D., Ye, Z., Gan, Q., Li, M., Song, X., ... & Zhang, Z. (2019). Deep graph library: A graph-centric, highly-performant package for graph neural networks. arXivpreprint arXiv:1909.01315.
- Fey, M., & Lenssen, J. E. (2019). Fast Graph Representation Learning with PyTorch Geometric [Computer software]. https://github.com/pyg-team/pytorch_geometric
- Godwin*, J., Keck*, T., Battaglia, P., Bapst, V., Kipf, T., Li, Y., ... Sanchez-Gonzalez, A. (2020). Jraph: A library for graph neural networks in jax(Version 0.0.1.dev). Opgehaalvan http://github.com/deepmind/jraph
- Hu, W., Fey, M., Zitnik, M., Dong, Y., Ren, H., Liu, B., ... & Leskovec, J. (2020). Open graph benchmark: Datasets for machine learning on graphs. arXivpreprint arXiv:2005.00687.