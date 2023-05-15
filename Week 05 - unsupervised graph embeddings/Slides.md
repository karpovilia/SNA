---
marp: true
theme: hahnec
size: 4K
paginate: false
footer: '[![](http://www.christopherhahne.de/images/favicons/apple-touch-icon-72x72.png)](http://www.christopherhahne.de)[Christopher Hahne](http://www.christopherhahne.de)'
header: '[&#9635;](#1, " ")  &nbsp; Title'
---

# Графовые эмбеддинги
### Subheading
Moscow, 2023
[video](https://youtu.be/nnvgnxFy6H8)
<!-- centered headline only on front slide -->
<style scoped>
  section{justify-content: center;}
</style>

---
## Graphs representation
![](Pasted%20image%2020230511141856.png)
In many fields the data have a graph structure
- social: friendship graph in social networks, graph of scientific citations
- man-made: internet, web, road networks, air communication networks
- In biology: protein interactions, complex molecules.

Machine learning tasks on graphs and their applications

- supervised, semi-supervised
	- node classification
		- Is the account a bot
		- Predicting user age, gender, profession in a social network
		- Predicting the function of a new protein based on its interaction with others
		- article topic prediction on the basis of citations
	- link prediction
		- content recommendation in an online platform
		- forecasting drug side effects
	- community detection
		- searching for users with similar interests
		- Revealing functional groups of proteins

**Objective:** extract features from the graph in a form suitable for machine learning algorithms

---

## Approaches to learning graph representations
![](Pasted%20image%2020230511141831.png)
**Task:** find a representation of graph vertices as vectors of (low-dimensional) space that preserve useful information. Normally, vectors are close in space if the vertices are close in the graph

graph embedding ~ representation learning

**Approaches:**
1. Based on matrix decompositions;
2. Based on random walks;
3. Graph neural networks.

---
## 1. Matrix Decomposition

Node representation as a dimensionality reduction problem with information preservation.

![](/img/Pasted%20image%2020230511143436.png)

**General idea:** represent the graph as a matrix and decompose it.

[SVD example](https://colab.research.google.com/drive/1q4MDNbBXtSDiscUwH4ftWYQEBrYercn4?usp=sharing)

*Notation:*
$G(V,E)$ - graph with vertices $V$ and edges $E$
$W$ - adjacency matrix with weights
$D$ - diagonal degree matrix
$L = D - W$ - Laplacian of the graph
$Y_i$ is the vector representation of a vertex $i$ of dimension $d \ll |V|$
$I$ is a unit matrix
$\phi(Y)$ - loss function

### 1) Locally Linear Embedding (2000)
$Y_i \approx \sum\limits_j{W_{ij}Yj}$
$\phi(Y) = \sum\limits_i{||Y_i - \sum{W{ij}Yj}||^2}$
is reduced to finding the smallest eigenvectors of the sparse matrix 
$(I-W)^T(I-W)$

### 2) Laplacian Eigenmaps (NIPS, 2002)

**Idea:** vertex representation is close if the vertices are connected
$\phi(Y) = \frac{1}{2}\sum\limits_{i,j}{||Y_i - Yj||_2^2W_{ij}} = Tr(Y^TLY)$
$Y^TDY = I$
is reduced to finding the smallest eigenvectors of the normalized Laplassian 

$L_{norm} = D^{-1/2}LD^{-1/2}$

3) Cauchy Graph Embeddings (ICML 2011)
Другая метрика близости $distance = \frac{|Y_i - Y_j|^2}{|Y_i - Y_j|^2+\gamma^2}$
$\phi(Y) = \frac{1}{2}\sum\limits_{i,j}\frac{W_{i,j}}{|Y_i-Y_j|^2+\gamma^2}$

The main problem is maintaining only 1st order proximity

*Definitions:*
First-order proximity between vertices $i$ and $j$ = edge weight $W_{ij}$
Let $s_i=[s_{i1},s_{i2},s_{iN}]$ be the $k$-order closeness. Then the $(k+1)$order closeness between vertices $i$ and $j$ = the similarity measure of vectors $s_i$ and $s_j$.


### 4) GraRep (CIKM, 2015)
Normalized transition matrix $X^k_{i,j}=log\frac{A^k_i,j}{\sum\limits_iA^k_{i,j}}-\log\beta$
$\phi(Y)=||X^k-Y_s^kY_t^{kT}||^2_F$
The representations for all k are concatenated. The disadvantage is the complexity of the algorithm $O(|V|^3)$.

### 5) HOPE, AROPE
Take S proximity matrix instead of adjacency matrix (Katz Index, Rooted Page Rank, Common Neighbors, Adamic-Adar score)

![[Pasted image 20230511165035.png]]

$\phi(Y)=||S-Y_sY_t^T||^2_F$ , сложность алгоритма $O(|E|d^2)$

Основные недостатки алгоритмов матричного разложения:
сохранение близости только 1-го порядка и/или большая сложность алгоритма

- HOPE [paper](https://www.kdd.org/kdd2016/papers/files/rfp0184-ouA.pdf)
	- [authors’ code](https://github.com/ZW-ZHANG/HOPE) (MATLAB)

![[Pasted image 20230511165532.png]]
- AROPE [paper](https://pengcui.thumedialab.com/papers/NE-ArbitraryProximity.pdf)
	- [authors’ code](https://github.com/ZW-ZHANG/HOPE) (MATLAB + Python)

---
## Word2vec
![](Pasted%20image%2020230511152227.png)



word2vec learns vector representations of words, useful in application tasks. Vectors show interesting semantic properties. For example:
-   _king: male = queen: female_ ⇒
-   _king - man + woman = queen_

 ![[Pasted image 20230511162541.png]]
[word2vec explanation](https://www.youtube.com/watch?v=UqRCEmrv1gQ)
[word2vec seminar ](https://colab.research.google.com/drive/17EOufnbX0fIIptUvx24P17seVVnyh1c_?usp=sharing)
![w2v](https://cdn-images-1.medium.com/max/2600/1*sXNXYfAqfLUeiDXPCo130w.png)



---
## 2. Random walks
**Key Idea**: Nodes in random walks $\approx$ words in  sentences -> use word2vec.

![[Pasted image 20230511162819.png]]

### 1) Deepwalk (KDD, 2014)
![[Pasted image 20230511162852.png]]

- Parameters
	- In practical tasks $w = 10$, $\gamma=80$
	- newer change $w$
	- If you lower $w$, increase $\gamma$

- DeepWalk [paper](https://arxiv.org/abs/1403.6652) 
	- [authors’ code](https://github.com/phanein/deepwalk) (Python) 
	- [C++ code](https://github.com/xgfs/deepwalk-c) 

### 2) LINE
**Key Idea:** - don't generate random walks

![[Pasted image 20230511164350.png]]

- LINE [paper](https://arxiv.org/abs/1503.03578)
	- [authors’ code](https://github.com/tangjianpku/LINE) (C++)

## 3) Node2vec
![[Pasted image 20230511164518.png]]

Low q - explore intra-cluster information
High q - explore inter-cluster information
	
- node2vec [paper](https://arxiv.org/abs/1607.00653) 
	- [authors’ code](https://github.com/aditya-grover/node2vec) (Python)
	- [C++ code](https://github.com/xgfs/node2vec-c)

## VERSE
Random walks define a hidden similarity distribution

![[Pasted image 20230511164714.png]]

 - VERSE [paper](https://arxiv.org/abs/1803.04742)
	 - [authors’ code](https://github.com/xgfs/verse) (C++)


## Useful Links
- Survey on graph embeddings and their applications to machine learning problems on graphs [peerj](https://peerj.com/articles/cs-357/)




- RandNE [paper](https://arxiv.org/abs/1805.02396)
	- [authors’ code](https://github.com/ZW-ZHANG/RandNE) (Python)
	
- FastRP [paper](https://arxiv.org/abs/1908.11512)
	- [authors’ code (Python)](https://github.com/GTmac/FastRP) [DEAD] 

 - NodeSketch [paper](https://exascale.info/assets/pdf/yang2019nodesketch.pdf)
	 - [authors’ code](https://github.com/eXascaleInfolab/NodeSketch)
	