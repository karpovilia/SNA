# Link to GitHub Predicting users' political views using ego graphs (Arsen Babochiev, Vikenty Bobrov, Alexandra Karmazina)

GitHub

# Description (CP)

## 1. Title

Predicting users' political views using ego graphs.
## 2. Abstract

This project aims to predict a user's political views on the Russian social network VKontakte using ego-network analysis. Ego-network analysis examines the relationships between an individual ("ego") and their immediate connections.

The goal is to develop a machine learning model that can forecast a VKontakte user's political stance. To achieve this, we will utilize ego-network analysis techniques and machine learning algorithms.

The proposed approach involves collecting social network data from VKontakte users and constructing their ego-networks based on connections. Machine learning models will then be trained on features extracted from the ego-networks to predict political views. Predictions will be evaluated based on accuracy.

## 3. Introduction

Social networks have become an integral part of modern life, with billions of users worldwide connecting and sharing information online. As these platforms continue to grow in size and influence, understanding user behaviors and relationships has taken on new importance. One area that could benefit from social network analysis is political science - by examining how views spread through social ties, we may gain insights into ideological diffusion and polarization.

This project aims to apply network science techniques to predict the political leanings of users on the Russian social media platform VKontakte. VKontakte boasts over 100 million monthly active users, making it one of the largest social networks in Europe. As with other sites, political content and discussions are common on VKontakte. 

We propose using ego-network analysis of VKontakte profiles to develop a machine learning model for political stance classification. Ego-networks model the ties of an individual ("ego") and their direct connections. By extracting features from users' ego-networks, such as tie strengths, clustering, and centrality measures, we hypothesize that machine learning algorithms can learn to predict a user's position on political issues based on their social relationships.

The potential applications of such a model are wide-ranging. It could provide insights for political campaigns seeking to activate supporters online. Marketers may find value in audience segmentation by inferred views. And from an academic perspective, the model could offer a novel lens for studying ideological diffusion through digital networks in Russia. Overall, the project aims to further our understanding of social influence processes and their relationship to real-world political attitudes.

## 4. Anticipated SNA Methods:

- Ego-Network Construction - Build ego-networks for each user based on their friend connections extracted from VKontakte profile data.
- Centrality Scoring - Calculate in-degree, out-degree, betweenness, closeness, and eigenvector centrality for each user in their ego-network to identify influential connections.
- Clustering Coefficients - Measure clustering/transitivity of connections within each ego-network to quantify local network structure.
- Homophily Analysis - Analyze similarities between connected users based on available profile attributes to understand propensity for homophilous ties.
- Link Prediction - Use network features to predict missing or future ties between users not yet connected.
- Community Detection - Identify densely connected groups within ego-networks that may represent real-world communities.
- Graph Embeddings - Generate vector representations of users/nodes based on network structure using models like node2vec for use in machine learning.
- Temporal Analysis - Analyze changes in network features over time that could signal shifts in political opinions.

## 5. Expected Outcomes

This project will provide insight into VKontakte user connections and allow us to develop a predictive model. Such a model could have applications in areas like marketing, social research, and content personalization. We hope our research and results will help improve forecasting and understanding of VKontakte user characteristics, as well as lay the groundwork for future network analysis studies and developments.

## 6. Dataset Requirements

To build the ego-network models and train the machine learning algorithms, we will need access to VKontakte user profile data as well as connection data showing each user's social ties. Key data points will include:

- User demographic information;
- Each user's full list of connections;
- Connection metadata like friend count, group memberships, etc;
- The dataset will be collected through VKontakte's API or via scraping public profile pages if needed. Data collection and storage will need to handle potential scale issues to ensure feasibility.