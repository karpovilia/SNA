## Why
Our goal is to assign our nodes meaningful coordinates (embeddings)
	coordinates allow us to create decision boundaries for classification problems
An embedding of a node should consider it's connections
	i,e, nodes that share many connections should have similar embeddings

![[1_XZQd9AfalvGWqy3ULVApog.webp]]

## Example 
- Nodes: people
- Node features: age, net worth
- Edges: in phone contacts
- Edge features: number of phone calls in last year
![[Pasted image 20230525135158.png]]
## Intuition
- **Goal**: to calculate neighborhood-aware embeddings for nodes
- **Approach:** 
	- Messages are sent between nodes via the edges
	- Nodes use these messages to update its embedding

![[Pasted image 20230525135742.png]]

### Framing the problems
- **Message** function - computes the message using node/edge features
- **Aggregation** function - combines the set of messages into a fixed-length vector that represents the neighbourhood
- **Update** function - computes new node embeddings using aggregated messages and the old node embedding

## Message function
![[Pasted image 20230525140714.png]]
$m_{i,j}^{(k)} = M(h_i^{(k)}, h_j^{(k)}, e_{ij})$ 
![[Pasted image 20230525140922.png]]
### Message function examples
- $m_{i,j}^{(k)} = M(h_i^{(k)}, h_j^{(k)}, e_{ij})$ 
- $m_{i,j}^{(k)} = h_j^{(k)}$  - Neighbor copy
- $m_{i,j}^{(k)} = \frac{h_j^{(k)}}{|N_j|}$ - Normalized neighbor copy
- $m_{i,j}^{(k)} = \alpha(h_i^{(k)}, h_j^{(k)})h_j^{(k)}$ - Attention

## Aggregation function
$\hat{m} = \oplus_{j\in N_i}m_{i,j}^{(k)}$
aggregate all the messages from the neighborhood of i
![[Pasted image 20230525142043.png]]
## Aggregation function properties
- Fixed-lentgh representation regardless of neighborhood size
![[Pasted image 20230525142052.png]]
- Permutation invariant: gives the same answer regardless of how you order the inputs
![[Pasted image 20230525142342.png]]
### Aggregation function examples
- $\hat{m}_{i,j}^{(k)} = \oplus m_{ij}^{(k)}$
- $\hat{m}_{i,j}^{(k)} = \sum\limits_{j \in N_i} m_{ij}^{(k)}$        - Sum
- $\hat{m}_{i,j}^{(k)} = \frac{1}{|N_i|}\sum\limits_{j \in N_i} m_{ij}^{(k)}$ - Average
- $\hat{m}_{i,j}^{(k)} = \max \limits_{j \in N_i} m_{ij}^{(k)}$       - Max

## Update function
$h_i^{(k+1)}=\varphi(h_i^{(k)}, \hat{m}_{i}^{(k)})$
![[Pasted image 20230525143127.png]]

### Update function examples
- $h_i^{(k+1)} = \varphi(h_i^{(k)}, \hat{m}_{i}^{(k)})$
- $h_i^{(k+1)} = \sigma(W^{(k+1)}, \hat{m}_{i}^{(k)})$
- $h_i^{(k+1)} = \sigma(W^{(k+1)}_{self}h_i^{(k)} + W^{(k+1)}_{neigh}\hat{m}_{i}^{(k)} + b^{(k+1)})$
- $h_i^{(k+1)} = \sigma(W^{(k+1)}, CONCAT(h_i^{(k)}\hat{m}_{i}^{(k)}))$


## Architecture examples - GCN
- $h_i^{(k+1)} = \sigma(W^{(k+1)}, \hat{m}_{i}^{(k)})$
- $\hat{m}_{i,j}^{(k)} = \sum\limits_{j \in N_i} m_{ij}^{(k)} = \sum\limits_{j \in N_i}  \frac{1}{c_{ij}}h_j^{(k)}$ 
- $h_i^{(k+1)} = \sigma(W^{(k+1)}\sum\limits_{j \in N_i}  \frac{1}{c_{ij}}h_j^{(k)})$

### Examples in code - GraphSage
$h_i^{(k+1)} = \sigma(W^{(k+1)}CONCAT(h_i^{k},\frac{1}{|N_i|}\sum\limits_{j \in N_i}h_j^{(k)}))$

https://docs.dgl.ai/guide/nn-forward.html#message-passing-and-reducing

https://docs.dgl.ai/en/0.8.x/generated/dgl.nn.pytorch.conv.SAGEConv.html

## Limitations
Bronshtein...
How powerfull are graph neural  networks
![[Pasted image 20230525145053.png]]




