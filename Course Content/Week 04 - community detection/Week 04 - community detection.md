Week 04 - Community detection

* [Описание курса](Course_SNA-2024.md)
* [Страница курса](https://karpovilia.github.io/SNA/readme/)

|Date|Time|Activity|Topic|Materials|
|----|----|--------|-----|---------|
| 26.09.2024 | 18:10-19:30 | Lecture 04 | |  [слайды](https://slides.com/karpovilia/deck), [видео Youtube](https://youtu.be/-rSOjAN3S-E), [видео Rutube](https://rutube.ru/video/private/2df4003221a7875886091b030e7fc09e/?p=iXSzCGbaUfscVDSqdnx9cg)|

## Practice
- [Simple communities](https://colab.research.google.com/drive/1ayB9aAXKMUDJFl7-g07nVXXobb74C5Iz?usp=sharing)
- [Better visualizations on larger graphs](https://colab.research.google.com/drive/1apjW45Du5fUxH4nN93gUD2DG0JWyY2X7?usp=sharing) 
- [Markov Clustering Algorithm](https://colab.research.google.com/drive/1VKFqnFvuTmqJWZdArcIMwypZBYu0R-Zi?usp=sharing)
- [Bayan_minimal_working_examples](https://colab.research.google.com/drive/1QJQRmM-6Zav9eLjh8Ve-hGSU96A70U7P?usp=sharing) 
- [Blockmodelling](https://colab.research.google.com/github/CALDISS-AAU/sdsphd19_coursematerials/blob/master/wednesday_network-blockmodeling/Lab_Blockmodeling.ipynb)
- [Leidenalg](https://colab.research.google.com/drive/1IgtOxzuzira4HwpOLReR0-vcwEZhtJbC?usp=sharing)

## References:
- Stochastic Block Modelling [youtube](https://www.youtube.com/watch?v=_-Z3WLkH_es)
- [From Louvain to Leiden: guaranteeing well-connected communities](https://www.nature.com/articles/s41598-019-41695-z), V. A. Traag, L. Waltman & N. J. van Eck, [pdf](https://www.nature.com/articles/s41598-019-41695-z.pdf)
- [20 years of network community detection](https://www.nature.com/articles/s41567-022-01716-7), Santo Fortunato, M. E. J. Newman, [pdf](https://arxiv.org/abs/2208.00111)

# Community Detection
Community Detection Metrics
- Various goodness metrics that evaluate structural properties of communities [1].
- Density - fraction of internal edges out of total number of possible edges.
- Conductance - fraction of total edge volume that points outside the cluster.
- Modularity - the difference of the number of edges in a community and the expected number of edges (assuming you have an identical degree distribution).

## Metric: Density
$$D(S) = \dfrac{2E_s}{|S|(|S|-1)}$$
### Example
$$ D({1,2,3,4}) = \dfrac{2\times5}{4(4-1)} = \dfrac{10}{12} $$

![[Pasted image 20230117145249.png]]

## Metric: Conductance
- Measure of internal and external connectivity. The fraction of edges pointing outside a community
$$C(S) = \dfrac{O_s}{2E_s+O_s}$$
$$C(S) = \dfrac{3}{2\times5+3} = \dfrac{3}{13}$$

## Metric: Modularity
- a global metriic: defined per-network, not per-community
- Measure of internal and external connectivity. How well network partitions into modules
- Higher values are better

$$ \mathbb{Q}(\mathbb{C})  = \dfrac{1}{2|E|}\sum_{u,v \in V}\left(A_{u,v}-\dfrac{d_u d_v}{2|E|}\right)\delta(\mathbb{C}_u\mathbb{C}_v)$$


- $\dfrac{1}{2|E|}$ - normalize by degree sum
- $\sum_{u,v \in V}(A_{u,v}-\dfrac{d_u d_v}{2|E|})$ - sum goes through every pair of verticies
- $A_{u,v}$ == 1 if adjacent, else 0
- $d_u$ - degree of $u$
- $\delta(\mathbb{C}_u\mathbb{C}_v)$ - [Kronecker delta](https://en.wikipedia.org/wiki/Kronecker_delta) function == 1 only if $u$ and $v$ are in the same community

![[Pasted image 20230117152218.png]]
|     | v=1               | v=2               | v=3               | v=4               |
| --- | ----------------- | ----------------- | ----------------- | ----------------- |
| u=1 | (0 - (2\*2)/8)\*1 | (1 - (2\*2)/8)\*1 | (0 - (2\*3)/8)\*1 | (0 - (2\*1)/8)\*0 |
| u=2 | (1 - (2\*2)/8)\*1 | (0 - (2\*2)/8)\*1 | (1 - (2\*3)/8)\*1 | (0 - (2\*1)/8)\*0 |
| u=3 | (1 - (3\*2)/8)\*1 | (1 - (3\*2)/8)\*1 | (0 - (3\*3)/8)\*1 | (1 - (3\*2)/8)\*0 |
| u=4 | (0 - (1\*2)/8)\*0 | (0 - (1\*2)/8)\*0 | (1 - (1\*3)/8)\*0 | (0 - (1\*1)/8)\*1 |

## Modularity - Values
- Modularity bounded in range [-0.5, 1]
- All nodes in a single community or all nodes in their own community $\rightarrow$ $Q=0$
- Nonzero values represent deviations from randomness (for better or worse)
- values > 0.3 is an indicator of good community structure

## Modularity: Another Equation

$$ \mathbb{Q}(\mathbb{C})  = \dfrac{|E(c)|}{2|E|} - \left(\dfrac{\sum_{u \in c}d_v}{2|E|}\right)^2$$


## Modularity: Directed and Weighted
Weighted
$$ \mathbb{Q}(\mathbb{C})  = \dfrac{1}{2|W_E|}\sum_{u,v \in V}\left(A_{u,v}-\dfrac{d^w_u d^w_v}{2|E|}\right)\delta(\mathbb{C}_u\mathbb{C}_v)$$

Directed: 
- o - outgoing edges
- i - ingoing
$$ \mathbb{Q}(\mathbb{C})  = \dfrac{1}{|E|}\sum_{u,v \in V}\left(A^o_{u,v}-\dfrac{d^o_u d^i_v}{|E|}\right)\delta(\mathbb{C}_u\mathbb{C}_v)$$




