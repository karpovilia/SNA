A reminder on possible tasks on graphs:

-   Node classification: some notes are labeled, but not all; we want to label unlabeled nodes.
-   Link prediction: some edges are unknown; we want to guess them.

Typical part of a data science pipeline: Feature engineering (from raw data to something that can be used). 80% of effort during DS development :) It would be nice to learn features automatically. And that something DL is supposed to be able to do. But how to apply it to graphs? Can we avoid engineering all these graph features manually?

Ultimately we want graph → vector pipeline. Feature representation embedding. Probabily node → vector (and then we can deal with vectors for diff nodes later). We want:

-   similar nodes have different representations.
-   network info be recorvered from node representations (through summing, averaging, pooling?)
-   this process to be parallelizable

Even a typical 2D representation of a graph for visualization purposes may be considered a simple case of node representation, as node position in (x,y) depends on its connections, and may resolve communities (if the graph is small / sparse enough, like the Karate club z.B.)

Key problem with graphs: no single reference point, aka **isomorphism problem**. You can permute a lot, and it's still the same graph supposedly. (Not the case with images, text, or audio).

Consider graph G(V, E), A is the adjacency matrix (no weights, no node features for now)

Encoder: enc(v) → z ∈ Rd�� (embedding space). d (dimension) is either custom, or default, but usually in the order of 10^2.

Two **similar** nodes should have high dot product ⟨ zi, zj ⟩ = ziᵀzj. In practice, "Similar" needs to be defined to better reflect your particualr task, but some common themes include:

-   connected
-   share neightors
-   have "similar roles within a graph, e.g. similar positions within a motif"
-   external properties (features, labels)

## Random walks - microscopic look[](https://www.kaggle.com/code/arsenykhakhalin/graphs-lecture-7-embeddings/notebook#Random-walks---microscopic-look)

**Shallow encoder**: embedding lookup, enc(v) = Zv where v is an indicator vector, and Z is essentially a table describing nodes. Matrix Z will be optimized to drive a loss down. Examples: DeepWalk, node2vec, TransE

**Random walk approaches**: for every node, generate a bunch of random walks starting from this node (aka "random walks with restart"). How many walks to run, and what the stopping criteria a, would form a strategy (R). A simplest strategy would be to just run lots of short random walks of fixed length L; a fancier strategy may include some adaptive sampling / exploration.

Simplest situation: If we are going after co-location in a graph, we can expect two nodes v and u co-occur within random walks if they are located "close" to each other. Each random walk is a sequence, or a multi-set (like a set, but each element may be present several times, as we may cycle and visit every node more than once).

> They claim that random walks are efficient, as they are local, and so allow us to work with very large graphs, aka they scale well. A natural question perhaps is why not use some flow-based approach; why keep it discrete. Isn't it a bit lazy? Or is there a real practical or theoretical benefit here?
> 
> The answer here is that you cannot afford to look at the full neighborhood, as it exponentially explodes, so you have to use some heuristic to prune it, in which case it's not different practically from a smart (aka "biased") random walk exploration strategy. I.e. if you explore the "let's not do random walks" strategy honestly, you'll proably converge on a very similar practical solution. Moreover, in practice random walks are often simulated.
> 
> So a follow-up question: how to implement (or simulate) random walks in practice, effeciently?

Because IRL most networks follow a power-law distribution, neighborhoods of each node quickly grow very large.

We want to find the vector embeddings z_u ∈ Rd�� to maximize log-likelihood ∑ulogP(NR(u)|zu)∑�log⁡�(��(�)|��) where NR�� is a neighborhood of node u obtained via strategy R. We define loss as L=−∑u∈V∑v∈NRlogP(v|zu)�=−∑�∈�∑�∈��log⁡�(�|��) , and eventually we'll be using SGD on it.

The probability here may be calculated using a sofmax: P(v|zu)=exp(z⊺uzv)/Σiexp(z⊺uzi)�(�|��)=exp⁡(��⊺��)/Σ�exp⁡(��⊺��)

> At this point I don't have a good intuition for how it can help to identify motifs (nodes that are very far from each other, but are very similar in terms of their topological context).

The problem with the expression above is that we have to loop through too many nodes in the denominator here (normalization term). We cannot afford it, so we need to approximate it. Solution: **negative sampling**:

logexp(z⊺uzv)Σiexp(z⊺uzi)≈log(σ(zu⋅zv))−∑i∈Slog(σ(zu⋅zi))log⁡exp⁡(��⊺��)Σ�exp⁡(��⊺��)≈log⁡(σ(��⋅��))−∑�∈�log⁡(σ(��⋅��)) where σ is a sigmoid function, and S is sampled from all nodes in some representative way. Normalize againt a negative sample. This is simple to word2vec: noise-contrastive estimation. And now we have linear complexity. How to sample? Typically, proportional to a node degree; sample sizes k~5-20.

It is also important to bound z_u, or trying to maximize dot-products, z vectors will try grow to inf, and we don't want it.

> Why sigmoid function, intuitively? One reason is that we want to take a log of it, and zi∙zj are between -1 and 1 (assuming that the are normalized), so we need to force them within 0,1. But why not exp() as in original softmax?
> 
> Why sampling proportional to degree? Does it come from some info about how real random walks behave?
> 
> Potentially, a good homework: check empirically that sampling proportional to node degree makes sense.

## node2vec - macroscopic look
**How to perform random walks?** Easiest approach: fixed length. Cannot go beyond "nodes are close to each other in the graph". One possible solution: **node2vec** that uses biased 2nd order walks. Can be seen as a trade-off between BFS (very local, microscopic) and DFS (in real (small-world) graphs, quite global).

Two parameters:

-   p (aka **return parameter**): probability of returning back to the previous node
-   q (aka **in-out parameter**): a ratio of BFS-style and DFS-style transitions.

In practice, they use unnormalized probability 1 for BFS-style step (sample another node that is connected both to the current node and to the previoud node), and 1/q for DFS step (go to a node that is no longer connected to the previous node). And an unnormalized probabiliy 1/p for a back-step. A distribution of co-occurrence of nodes in a random walk is now a function of these two parameters (p, q). Ref: Grover 2016.

> Still not sure how it can help with motifs. It probably cannot?

A cool thing is that both random walks implementation and minimization are parallelizable.

What to do next?

-   **Label nodes**: Train a classifier z_v → label
-   **Cluster** z_v and predict communities
-   **Link prediction**: use some type of an aggregation function for 2 z-values, then train a classifier on them. Options for aggregators: concat, hadamard, sum/average, distance between two z. Depending on the task, some of these options may work much better than the others.

> Any good intuition for when one would be better than the other? Can we find 4 intuitive examples when each of these 4 aggregation options would work better than the other three?

### Knowledge graphs - semantic embedding

**TransE**: an alternative approach that doesn't actually rely on random walks. Ref: Borders 2013.

We have a bunch of objects (for example, books, authors, genres, usually referred to as **entities**), and edge connecting them, that correspond to predicates (like, this book belong to this genre, usually called **relations**), and there are many different types of links. The task we have is **graph completion**, or guessing links that are missing.

**Translating embeddings**: relationships are represented as triplets (h, l, r) = (head entity, relation, tail entity). Entities are embedded in entity space Rkℝ� (k~50 for a dataset with ~1000 different relation types!!). Relationships are represented as translations in this entity space: h+l ≈ t if the relationship is true (so l∈Rk�∈ℝ� as well, but they have a distribution of their own)

> This sounds similar to word2vec idea of king-male+female = queen. But how is it possible that a dataset with so many different types of relationships (Freebase, ~1000 types of edges) can be successfully presented in a space so much flatter (only k~50 dimensions? How is it even possible? Would not it mean that very different relationship types (genre, author) have to "share" dimensions (subspaces, hyperplanes)? How can they avoid conflicts?

We initialize entities e_i as a uniform distribution. Translation vectors are init as uiform, then normalized (so uniform on a sphere).

Then we use contrastive loss (aka triplett loss): at each step we move 2 related items closer to their "target positions" (based on the meaningful translation l), and 2 unrelated (randomly sampled) items further apart. The gradient is given by the formula:

∑∇[γ+d(h+l,t)−d(h′+l,t′)]∑∇[γ+�(ℎ+�,�)−�(ℎ′+�,�′)] where (h,l, t)is a positive sample, (h', l, t') is a negative sample, and d is a distance between the target point h+l and the actual point t (**dissimilarity measure**: in practice either L1 or L2 norm). We perform SGD on both entites and translations. Every now and then (after each minibatch of triplets) we also normalize all entity vectors e ← e/||e||.

When sampling negative elements, we do not care about the "type" of these elements; we sample completely at random, which is the whole point. For example, if a correct statement is (Paris , is the capital of, France), then we don't hunt for h' and t' that would make the statement "incorrect but sensible" (London, is the capital of, Romania). We sample entities completely at random (JKRowling, is the capital of, bird), and that's the whole point, as it will eventually align values "properly". Typically, in practice, we keep either head or tail the same as for the "positive triplet", and only randomly sample the other element.

"Sibling relationships" (both A and B are written by X) are represented by points that are very close to each other, at least within some hyperplane.

> How do translation vectors get to be distributed even tually? Are similar relationships (in some semantic way) co-aligned? Or is it the other way around, and it is very dissimiarl relationships that are forced to share a hyperplane, as if there's no overlap between the items that engage in these relationships, and so there's no chance for a mistake? Say, if "being a capital of" and "having made of" are co-aligned, we may never notice it, as London is not made of anything in particular, and a spoon is a capital of no country. Is it what makes a low-dim embedding possible to begin with?

### Embedding entire graphs

Once you embedded nodes meaningfully, how do you embedd an entire graph, to classify them? One option: just sum all vectors together, then build a classifier on this.

You can also do similar summarization on subgraphs (like in graph condensation), then run a graph embedding again (now representing each **virtual node** (Li 2016) as a point). Repeat recursively?

**Anonymous walks** (2018): instead of preserving node identity, only look at how often you visit notes again (as in "one node, another node, the 1st node again, etc.") If you process all these anonymous walks together, it will tell you something about the character of your graph.

## Refs
- Standford Lecture: [https://www.youtube.com/watch?v=2XFMAdHa8uY&list=PL1OaWjIc3zJ4xhom40qFY5jkZfyO5EDOZ&index=6](https://www.youtube.com/watch?v=2XFMAdHa8uY&list=PL1OaWjIc3zJ4xhom40qFY5jkZfyO5EDOZ&index=6)
- https://www.kaggle.com/code/arsenykhakhalin/graphs-lecture-7-embeddings/notebook
- Node2vec: Grover, A., & Leskovec, J. (2016, August). node2vec: Scalable feature learning for networks. In Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining (pp. 855-864). (3k citations)
- Knowledge graphs: Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J., & Yakhnenko, O. (2013). Translating embeddings for modeling multi-relational data. In Advances in neural information processing systems (pp. 2787-2795). [http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf](http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf) (2.5k citations)
- On knowledge graphs, see also: Wang, Z., Zhang, J., Feng, J., & Chen, Z. (2014, July). Knowledge graph embedding by translating on hyperplanes. In Aaai (Vol. 14, No. 2014, pp. 1112-1119). (1k+ citations)