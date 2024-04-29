## Examples
- Predict if this molecule:
	- Is toxic
	- Activates a protein / Treats a disease
	- General properties of molecules
- Predict the biological taxonomy of a protein interaction network
- What type of object a point cloud represents
- The expression made by a face, represented as a mesh


## Overall Architecture
- Input features X for nodes and edges, when available
	- OPTIONAL: Preprocess features by passing through an MLP, shared across the nodes 
- Stack **GNN layers** to incorporate graph neighborhood information and get node embeddings 
- Use a **Readout** function to pool node-level embeddings into a graph-level embedding 
- Use the graph-level embedding to make a prediction (e.g., with an MLP) on the graph 
	- Loss functions are the standards: cross-entropy for classification tasks, mean-squared error for regression

## Graph Pooling
![[edu/Magolego 2024/Course Content/Week 08 - graph classification [old]/img/Pasted image 20230608180203.png]]

## Graph Pooling with Set Pooling
- Set pooling: map a set of embeddings to a single embedding 
	- I.e., $\{ℎ_i|i \in V\} \rightarrow h_G$
	- Does not consider graph topology
- Sets do not have a natural order and the operation should therefore be *Permutation Invariant*
	- Can use the same Permutation Invariant functions we used when creating node-neighborhood representations in GNNs: aggregation functions like SUM, MEAN, MAX, …, etc. 
	- E.g., $h_G = \sum\limits_{i \in V}h_i$

## Graph Pooling with Coarsening 
*Graph coarsening*: hierarchically cluster using graph structure 
- Iteratively down-samples, typically by clustering nodes and representing the cluster by a single embedding 
	- For each iteration, the adjacency matrix is changing.
- Clustering operation needs to be *differentiable* so operation can be used end-to-end
	- E.g. [Graph U-Nets](https://arxiv.org/abs/1905.05178), which projects nodes into 1-dimension using learnable linear layer and chooses k-largest ones as subset for next iteration.

## Nuances of Graph Batching 
- In previous tasks, we had one large graph and were sampling nodes and their k-hop neighborhoods 
- Now: 1 sample = 1 full graph, no edges between graphs in the batch 
- How should we do message passing? 
	- Could loop over each graph and run MP separately (slow)


## The batched “super-graph” 
- Alternatively, could create a “super-graph” that creates a block-diagonal adjacency matrix of disconnected components and run MP once (fast) 
- This creates book-keeping complexity of keeping track of which node belongs to which graph. This is important when need to do graph pooling to get graph-level embeddings 
- This is DGL’s approach and they provide tooling for managing this complexity (e.g., [Batching and Reading Out Ops](https://docs.dgl.ai/en/0.6.x/api/python/dgl.html))
![[edu/Magolego 2024/Course Content/Week 08 - graph classification [old]/img/Pasted image 20230608180328.png]]


## Graph Classification Exercise
- [ogbg-molhiv](https://ogb.stanford.edu/docs/graphprop/) dataset from Open Graph Benchmark: 
- Predict whether a molecule (graph) inhibits HIV replication 
- 41k molecules from [MoleculeNet](https://moleculenet.org/) 
- Average of 26 nodes and 28 edges per graph 
- Natural features for both atoms (nodes) and bonds (edges): 
- Categorical in nature and the features are therefore integers that indicate the category mapping for each column 
- List of features is [here](https://github.com/snap-stanford/ogb/blob/68a303f320220cda859e83e3a8660f2b9debedf6/ogb/utils/features.py), but include things like atomic number, bond type, …, etc. 
- OGB provides classes for converting these categorical/integer features into embeddings: [AtomEncoder](https://github.com/snap-stanford/ogb/blob/68a303f320220cda859e83e3a8660f2b9debedf6/ogb/graphproppred/mol_encoder.py) and [BondEncoder](https://github.com/snap-stanford/ogb/blob/68a303f320220cda859e83e3a8660f2b9debedf6/ogb/graphproppred/mol_encoder.py) 
- Split into train/val/test based on molecular structure 
	- To evaluate generalization, the test nodes have structural differences from those in the training set