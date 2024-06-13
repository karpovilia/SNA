- Observation: more layers = worse performance 
- Paradoxically, need more layers to capture long-range information
	- The number of layers needs to match the [Bottleneck of Graph Neural Networks](On%20the%20Bottleneck%20of%20Graph%20Neural%20Networks%20and%20its%20Practical%20Implications.md), which conceptualizes the distance away from a node that contains information important to the task.
- Adding layers often gives exponential increase in **receptive field** (i.e., you get the neighbors’ neighbors) – lots of information to capture since we need the neighbors of the neighbors of the neighbors.
![](Pasted%20image%2020240613142752.png)
Given a d-dimensional vector of 32-bit float values flatten each float into 32-digit binary vector to represent states: $Ω = 2^{32d}$
This gives an upper-bound on the number of structures a vector could possibly distinguish among. Capacity needed to fit training data of a toy problem:
![](Pasted%20image%2020240613143820.png)

- Adding fully-connected adjacency (“FA”) layers for final GNN layer (i.e., pretended graph was fully connected) consistently improved performance
	- This shows that there was meaningful info in other nodes that wasn’t captured by the multi-layered GNN
- However, using FAs in all layers (i.e., ignoring real graph structure) produced much worse results

![](Pasted%20image%2020240613144237.png)
Best improvement achieved for [GGNN](Gated%20Graph%20Sequence%20Neural%20Networks.md)'s
## Over-smoothing vs Over-squashing  
- **Over-smoothing**: node representations become indistinguishable when the number of layers increases due to taking aggregates of aggregates of… 
- **Over-squashing**: information from an exponentially-growing receptive field is compressed into fixed-length node vectors
	- Similar in concept to RNNs, which need to represent e.g., a sequence of words in a fixed-length vector, and this can become a bottleneck for long sequences

### Solution 1: Skip Connections 
High-level idea: copy/paste information from a lower layer so that the new layer doesn’t have to keep track of everything • Several different types… 
- Residual connection—connect $l − 1$ to $l$: $\hat ℎ^l = f(ℎ^l,ℎ^{l-1})$ 
- Initial connection—connect $l = 0$ to all $l$: $\hat ℎ^l = f(ℎ^l,ℎ^0)$ 
- Dense skip connection—connect $l′ < l$ to l: $\hat ℎ^l = f(ℎ^l,ℎ^{l'|l'<l})$ 
- Jumping Knowledge connection—connect all layers to the final layer: $\hat ℎ^L = f(ℎ^L,ℎ^{l|l < L})$

### Solution 2: Graph Normalization
- High-level idea: ”re-scale node embeddings over an input graph to constraint pairwise node distance and thus alleviate over-smoothing” [Bag of Tricks for Training Deeper Graph Neural Networks A Comprehensive Benchmark Study](Bag%20of%20Tricks%20for%20Training%20Deeper%20Graph%20Neural%20Networks%20A%20Comprehensive%20Benchmark%20Study.md)
- Several different types… 
	- [Batch Normalization](Batch%20Normalization%20Accelerating%20Deep%20Network%20Training%20by%20Reducing%20Internal%20Covariate%20Shift.md): normalize based on statistics of the minibatch 
	- [PairNorm](PairNorm%20Tackling%20Oversmoothing%20in%20GNNs.md): maintain consistent pairwise distance among nodes 
	- [NodeNorm](Understanding%20and%20Resolving%20Performance%20Degradation%20in%20Graph%20Convolutional%20Networks.md): normalize each node separately based on feature variation 
	- Other [tricks](Bag%20of%20Tricks%20for%20Training%20Deeper%20Graph%20Neural%20Networks%20A%20Comprehensive%20Benchmark%20Study.md)

### Solution 3: Graph Rewiring
- High-level idea : change the graph (edge set) to make it more message-passing friendly
	- There is no guarantee that the natural graph structure is equal to the one that expresses optimal computational dependencies
	- There are noisy edges, and some important relationships may not be captured by an edge
- Diffusion-based approaches: smooth A with a [diffusion process](Diffusion%20Improves%20Graph%20Learning.md) (includes multi-hop info) and sparsify to get a new A
- Geometric [“Ricci-curvature” approach](Understanding%20over-squashing%20and%20bottlenecks%20on%20graphs%20via%20curvature.md): selectively remove edges that bridge different communities, as this causes the exponential increase