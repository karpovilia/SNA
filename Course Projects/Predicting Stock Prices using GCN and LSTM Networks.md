by: 

GitHub
## 1. Key Idea of the Project 

The goal of this project is to develop an accurate predictive model for stock prices using a combination of Graph Convolutional Neural Networks (GCN) and Long Short-Term Memory (LSTM) networks. 
Predicting stock prices accurately is of paramount importance for investors and traders to make informed decisions and manage risks effectively. Traditional methods often rely on technical analysis and historical data. However, by leveraging the power of neural networks and graph analysis, we aim to create a more robust and accurate predictive model. 
Similar approaches combining graph analysis and neural networks have been used in various domains, including social network analysis, recommendation systems, and fraud detection. In recent years, the application of such techniques to financial data analysis, including stock price prediction, has gained attention. To achieve our goal, we plan to follow these steps: 
1. Data Collection; 
2. Graph Construction; 
3. Model Development. 
## 2. Dataset Required to Do the Project 

Historical stock price data will be collected from reputable financial data sources such as Yahoo Finance, Alpha Vantage, etc. The dataset should include features such as opening price, closing price, highest price, lowest price, and trading volume for a specific time period. Data should cover a sufficiently long time frame to capture various market conditions and trends. Data quality is essential for reliable predictions. Therefore, we will ensure that the data is accurate and free from errors. 

## 3. Anticipated SNA Methods 

• Graph Construction: Build a graph representation of the stock price data, where each node represents a price change, and edges connect consecutive price changes. This approach allows us to capture the sequential relationship between different price changes and represent the data in a structured format suitable for graph analysis. 
• Graph Convolutional Neural Network (GCN): Train a GCN to analyze the graph structure of the stock price data, capturing the relationships between different price changes. GCNs have been proven effective in analyzing graph-structured data and capturing complex relationships between nodes in the graph. 
• Long Short-Term Memory (LSTM) Network: Pass the output of the GCN to an LSTM network to capture temporal dependencies in the data and make predictions based on historical trends. LSTMs are wellsuited for capturing temporal dependencies in sequential data, making them ideal for analyzing time series data like stock prices. 
• Model Evaluation: Evaluate the performance of the combined GCNLSTM model using appropriate metrics. 
## References 

1. Feng, Fuli, et al. ”Temporal relational ranking for stock prediction.” ACM Transactions on Information Systems (TOIS) 37.2 (2019): 1-30. DOI: 10.1145/3309547 

2. Li, Zhishuai, et al. ”A hybrid deep learning approach with GCN and LSTM for traffic flow prediction.” In 2019 IEEE intelligent transportation systems conference (ITSC), IEEE, 2019. DOI: 10.1109/ITSC.2019.8916778