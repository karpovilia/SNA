by Manokhin Artyom

# Description (CP)

## Key idea of project

### Goal of the project

The key idea of the project is to understand how users of the social network X (Twitter) interact in the framework of discussing issues related to Islam. Based on this topic, it will be possible to draw a conclusion about how people are connected to each other within communities interested in Islamism.

### Why is it worth doing?

The study of user interaction in X can help us understand the dynamics of the formation of Islamist groups. As a result, it will be possible to highlight the features within this topic.

### Who did something similar before?

Previous studies have not been found on this topic.

### How are we going to reach the goal?

Thanks to our approach of modern social network analysis, analyzing social graphs X, connections will be visualized. Clustering will help to divide the network into communities according to the internal division of messages related to Islam.

## Dataset required to do the project

### Description & link

«Islam retweet networks» will be used for the analysis.

Link: [https://networkrepository.com/rt-islam.php](https://networkrepository.com/rt-islam.php "https://networkrepository.com/rt-islam.php")

### Limitations

Not all the data is presented here, but only a part. The analysis will be carried out based on the provided sample.

## Anticipated SNA Methods

### Network Construction

Nodes are twitter users and edges are retweets. These were collected from various social and political hashtags.

### Community Detection

State-of-the-art community detection algorithms: the Louvain, Girvan-Newman methods

### Centrality Analysis

Degree centrality will be applied to search users whointeract with others more often.

### Interaction Analysis

Type, frequency and other parameter will be usefull here

### Visualization

Gephi / NetworkX (Python)