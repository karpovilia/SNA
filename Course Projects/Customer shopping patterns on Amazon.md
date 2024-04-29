by Sofya Morozova, Anna Bondar, Ilya Polyakov (GitHub)
## Key Idea of Project:

**The goal of this project** is to analyse the purchasing behaviour of Amazon customers through social network analysis (SNA) techniques.

By leveraging the "Customers Who Bought This Item Also Bought" feature of the Amazon website, we aim to construct a directed graph representing the relationships between products based on their co-purchase frequency.

This project is worth pursuing as it offers valuable insights into consumer preferences, product associations, and potential recommendation strategies for e-commerce platforms. While similar studies have been conducted in the past focusing on social network analysis in various domains, such as online social networks and citation networks, our approach is unique in its focus on e-commerce data and specifically Amazon customer behaviour.

To achieve our goal, we will employ a combination of data preprocessing techniques, network analysis algorithms, and visualization methods.

## 3. Dataset required to do the project

Dataset link: [https://snap.stanford.edu/data/amazon0302.html](https://snap.stanford.edu/data/amazon0302.html)
Dataset statistics:

|                                  |                 |
| -------------------------------- | --------------- |
| Nodes                            | 262111          |
| Edges                            | 1234877         |
| Nodes in largest WCC             | 262111 (1.000)  |
| Edges in largest WCC             | 1234877 (1.000) |
| Nodes in largest SCC             | 241761 (0.922)  |
| Edges in largest SCC             | 1131217 (0.916) |
| Average clustering coefficient   | 0.4198          |
| Number of triangles              | 717719          |
| Fraction of closed triangles     | 0.09339         |
| Diameter (longest shortest path) | 32              |
| 90-percentile effective diameter | 11              |

**Scraping**: we don’t need scraping because we use an existing dataset.

**The limitations of the existing dataset:**

●     Limitations are that SNA offers a static view of the network and is not able to show dynamic aspects

●     Failure to verify the accuracy and reliability of data and its sources

●     Possibly (it will become clear after analysis) too large network size for analysis, which will lead to difficulties in analysis

## 4. Anticipated SNA Methods

One of the most common ways to analyze a network is to look at the centrality of various nodes to identify key players, information hubs, and gatekeepers across the network.

●     Degree Centrality: Can be used to identify the most connected actors in the network. These actors are considered “popular” or “active” and they often have a strong influence within the network due to their numerous direct connections.

●     Betweenness Centrality: A useful for identifying the “brokers” or “gatekeepers” in the network. These actors have a unique position where they connect different parts of the network, facilitating or controlling the flow of information between others.

●     Closeness Centrality: A measure of how quickly a node can reach every other node in the network via the shortest paths. In a coalition, these nodes can disseminate information or exert influence quickly due to their close proximity to all other nodes.

●     Clustering Coefficients: The Clustering Coefficient provides insights into the “cliquishness” or local cohesion of the network around specific nodes.

●     Structural Equivalence: Structural Equivalence is used to identify nodes that have similar patterns of connections, even if they do not share a direct link. Understanding structural equivalence can provide insights into the dynamics of the network, such as potential redundancies, competition, or opportunities for collaboration. It can also reveal how changes in one part of the network may impact other, structurally equivalent parts of the network.

●     Visualizing Networks:

	○     Overview of Network Structure

	○     Identification of Key Actors

	○     Detecting Subgroups and Communities

	○     Identifying Outliers and Peripheral Nodes

	○     Highlighting Network Dynamics

## 5. References (optional)

https://snap.stanford.edu/data/amazon0302.html

https://builtin.com/data-science/social-network-analysis

https://visiblenetworklabs.com/guides/social-network-analysis-101/