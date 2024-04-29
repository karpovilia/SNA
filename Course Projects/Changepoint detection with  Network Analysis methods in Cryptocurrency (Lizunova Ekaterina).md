## Link to GitHub Changepoint detection with Network Analysis methods in Cryptocurrency (Lizunova Ekaterina)

[GinHub](https://github.com/Katecorn/SNA_CPD_NA_project/tree/main?tab=readme-ov-file)

# Description (CP)

1. **Changepoint detection in Cryptocurrency with Network Analysis methods**
2. **Key idea of project**

**The main goal is to investigate the applicability of Networks methods for solving the problem CPD (change point detection) in time series.**

**Motivation:**

- CPD is useful for monitoring model performance, which can be applied to risk management in investment and strategy formulation.
- Incorporating changepoints in cryptocurrency price forecasting models can improve their accuracy.

**Examples of work are presented in the table with articles on github (Notion page).**

**Examples of hypotheses:**

- Changes in network structures (for example, changes in node centrality) may precede or accompany change points in the time series of cryptocurrencies.
- External points of change in cryptocurrency prices occur with key market events or network changes (e.g. new tokens, changes in the transaction network)

**3. Dataset required to do the project**

**Options for passing transaction data:**

- An API that, among other things, allows downloadingblocks and/or transactions
- Blocks and/or transactions are available (usually inJSON format) on certain web pages. In this case, once the indices of blocks corresponding to the desiredperiod of time are found, all one has to do is to iteraterequests to the site by using the right parameters.

**Possible problems:**

- there are coins for which it is impossible to obtain data in this format, for example, Monero
- download parallelization problem - speed limits, error “too many requests sent”
- the problem of calculating some metrics (the article said that calculating the average length of the shortest path may take several months)
- in general, a large amount of RAM is required to process data of such volume

**4. Anticipated SNA Methods**

- **Centrality Analysis:** Study of degree, closeness, betweenness and Egean centrality of cryptocurrencies to identify key nodes in the network.
- **Correlation analysis:** Analysis of correlations between the prices of various cryptocurrencies to understand the relationships between them.
- **Change Monitoring:** Monitors changes in network structures and time series of cryptocurrency prices to identify possible points of discord.

**We can try exploring Graph Neural Networks (GNN methods)**

**5. References (optional):**

**Datasets:**

- Транзакции криптовалют: [https://snap.stanford.edu/data/#cct](https://snap.stanford.edu/data/#cct)
- биткоин - есть разметка данных illigal activities: [https://github.com/git-disl/EllipticPlusPlus](https://github.com/git-disl/EllipticPlusPlus)[https://www.kaggle.com/datasets/ellipticco/elliptic-data-set](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set)
- **MBAL: 10 millions crypto address label dataset:** [https://www.kaggle.com/datasets/yidongchaintoolai/mbal-10m-crypto-address-label-dataset](https://www.kaggle.com/datasets/yidongchaintoolai/mbal-10m-crypto-address-label-dataset)
- **Top 100 Cryptocurrencies Historical Dataset (исключительно стоимости монет):**[https://www.kaggle.com/datasets/kaushiksuresh147/top-10-cryptocurrencies-historical-dataset](https://www.kaggle.com/datasets/kaushiksuresh147/top-10-cryptocurrencies-historical-dataset)
