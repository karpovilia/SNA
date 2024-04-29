## Enhancing Recommendation Systems using Knowledge Graphs and Graph Neural Networks 
by
- Kormishenkov Alexander
GitHub
### Key idea of project
I am really interested in Knowledge Graphs and their applications, therefore I want to try them in recommendation system for popular domains (movies, books, products). This project should help me in my further plans at work to apply KGs at bank product recommendations at Sber.  

- Goal: The goal of this project is to improve the accuracy and performance of recommendation systems by incorporating knowledge graphs and graph neural networks.

- Worth doing: This project is worth pursuing as it has the potential to enhance user experience, increase recommendation relevance, and provide more personalized recommendations.

- Similar work: I based my ideas on this article **A Survey on Knowledge Graph-Based Recommender Systems -** [https://arxiv.org/abs/2003.00911](https://arxiv.org/abs/2003.00911). There are a full information of methods for recommendations system. It is an old article, further I’ll find more actual articles and resources. 

- Reaching the goal: I plan to achieve this goal by first integrating knowledge graphs into the recommendation system to capture semantic relationships between items and users. I will then use graph neural networks to learn the representations of nodes in the knowledge graph and make better recommendations based on these learned representations .

### Dataset required:

- MovieLens
- Amazon-Book, DBbook2014
- Amazon Product data (I knew about Alibaba product knowledge graph, but it is on Chinese)
- Last.FM

### Anticipated Methods:

- I want to use techniques such as graph convolutional networks (GCNs) and graph attention networks (GATs) and methods for making embeddings for KG (TransE, DistMult, etc.). We will also (I believe I can do it) explore collaborative filtering methods and matrix factorization techniques to compare their recommendation performance with graphs methods.

### References: 

- [https://towardsdatascience.com/introduction-to-knowledge-graph-based-recommender-systems-34254efd1960](https://towardsdatascience.com/introduction-to-knowledge-graph-based-recommender-systems-34254efd1960)
- KG embeddings [https://pykeen.readthedocs.io/en/stable/index.html](https://pykeen.readthedocs.io/en/stable/index.html) 
- GCN and GAT [https://pytorch-geometric.readthedocs.io/en/latest/](https://pytorch-geometric.readthedocs.io/en/latest/)
- Classical libraries for recsys: lightFM
- Sber AI: [https://github.com/sberbank-ai-lab/RePlay](https://github.com/sberbank-ai-lab/RePlay)

If there are many project with recomendation systems, I can continue little project from my previous subject - [https://www.figma.com/file/EIFpI5zbeOkQhgGu1iRsZc/Graphs?type=whiteboard&node-id=0-1&t=yivX3QH39wTP3zLB-0](https://www.figma.com/file/EIFpI5zbeOkQhgGu1iRsZc/Graphs?type=whiteboard&node-id=0-1&t=yivX3QH39wTP3zLB-0)