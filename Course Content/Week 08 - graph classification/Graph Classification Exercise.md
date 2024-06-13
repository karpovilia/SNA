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