Many real-world/industrial graphs are billions of nodes and edges, perhaps 100s of billions
- E.g., E-commerce products, reviews, transactions, sign-in events
- You may not even be able to fit this into memory
In small-world graphs like social networks, ~6 GNN layers means every node in the graph is needed to calculate each node embedding.

## Sampling
We don’t need the full graph to compute useful embeddings
- In fact, having this source of randomness may make your model generalize betterto new, slightly different neighborhoods

We can sample at different levels:
- Subset of neighbors of each node during message passing
- A set of nodes for each GNN layer
- A subset of the graph for the full GNN


## Node-level Sampling
- Random neighbor sampling: for each node, only choose a subset of neighbors for message passing (e.g., [GraphSage](Inductive%20Representation%20Learning%20on%20Large%20Graphs.md)).
	- Still suffers from exponential growth with layers, but controllable
- Importance sampling: try to improve the variance of your estimate by smarter sampling
	- [FastGCN](FastGCN%20Fast%20Learning%20with%20Graph%20Convolutional%20Networks%20via%20Importance%20Sampling.md) and [LADIES](Layer-Dependent%20Importance%20Sampling%20for%20Training%20Deep%20and%20Large%20Graph%20Convolutional%20Networks.md) use importance sampling at the layer-level to reduce exponential growth to linear growth
## Subgraph sampling
- [Cluster-GCN](https://arxiv.org/abs/1905.07953): Find densely connected clusters and only sample neighbors in the same cluster
- [GraphSAINT](https://arxiv.org/abs/1907.04931) : Create random subgraphs for each minibatch and model with a GCN as if it were the full graph

## Pre-computation
- Idea: instead of doing message passing before each MLP layer, do graph-based processing once
- Assumes that the non-linearity between GNN layers is not important, so the model fitting phase is ~ logistic regression
- Can be done in one big batch-processing job, not during training process
- [Simple Graph Convolution](https://arxiv.org/abs/2007.02133) (SGC): $H=softmax(A^KX\theta)$
- [Scalable Inception Graph Neural Networks](https://arxiv.org/abs/2004.11198) (SIGN): Similar to SGC, but also consider general operators, not just powers of **A** (e.g., counting triangles, diffusion operators like [Personalized Page Rank](https://arxiv.org/pdf/2006.11876.pdf),..., etc) and concatenate results as features

## Resource management
- There are optimizations that can be made to improve resource utilization
- [GNNAutoScale](https://arxiv.org/abs/2106.05609) caches historical embeddings from previous minibatches to avoid re-computing them
- [ROC](https://www.cs.cmu.edu/~zhihaoj2/papers/mlsys20.pdf) and [DistGNN](https://arxiv.org/abs/2104.06700) enable fast/scalable distributed training via memory and graph partitioning optimizations