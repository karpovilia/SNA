# Link to GitHub Points of discourse identification using knowledge graphs in presidential speeches. The case of President Joe Biden’s speeches concerning foreign policy in 2023 (Novitskaya Alina, Melnikov Ivan)

GitHub

# Description (CP)
## 1. Title 
The title of our project is “Points of discourse identification using knowledge graphs in presidential speeches. The case of President Joe Biden’s speeches concerning foreign policy in 2023”. 

## 2. Key Idea 

The primary goal is to extract, analyze, and visualize the interconnectedness of topics, themes, and entities mentioned in these speeches, providing valuable insights into the administration's foreign policy priorities and strategies. This project is worth pursuing due to its potential to offer a detailed understanding of the presidential discourse on foreign policy, aiding policymakers, analysts, and the public in comprehending the administration's approach to global affairs. While similar studies have explored discourse analysis in political speeches, the application of knowledge graphs in this context is relatively novel, promising a more structured and comprehensive analysis. To achieve the project's objectives, we will employ natural language processing techniques to extract textual data from President Biden's speeches, construct a knowledge graph representing the relationships between entities and concepts, and then apply graph analysis algorithms to identify key points of discourse and visualize the results for interpretation and further analysis. 

## 3. Dataset 
We will apply scraping techniques and tools (Python) to build the dataset based on the videos of speeches of President Joe Biden that can be found on YouTube. We will take 10 most viewed speeches dedicated to foreign policy, for example, President Biden’s Address to the 78th United Nations General Assembly (URL: https://www.youtube.com/watch?v=Hnvasxoys60).

## 4. SNA Methods 
To complete this project we are going to collect and prepare the data for analysis, preprocess data, construct networks using discourse-based knowledge graphs and then analyze these networks. We are going to use the official videos with English versions of recorded speeches of President Joe Biden. The speech will be converted to text. To construct a network we are going to preprocess these texts by natural language processing technology: firstly, we will transform sentences into SOV form (subject-object-verb). Based on that version of the text we will build a network: nodes will be countries, geographical names, international organizations and persons, connections between them will be verbs. Next, we will analyze the constructed graph based on the studied SNA contents, such as: 
● Degree distribution; 
● Power law distribution; 
● Distance; 
● Network diameter; 
● Transitivity; 
● Average local CC; 
● Degree centrality; 
● Closeness centrality; 
● Betweenness centrality; 
● Eigenvector centrality; 
● etc. 

## 5. References 
1. Chen, Guangyuan, et al. Extracting Salient Discourse Events from Presidential Speeches Using a Structured Knowledge Base. Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. 
2. Chen, W., Zhang, X., Wang, T., Yang, B., & Li, Y. (2017, August). Opinion-aware Knowledge Graph for Political Ideology Detection. In IJCAI 3 (Vol. 17, pp. 3647-3653). URL: https://www.ijcai.org/proceedings/2017/0510.pdf 
3. Patricia Dunmire et al. Political Discourse Analysis: Exploring the Language of Politics and the Politics of Language. Language and Linguistics Compass 6(11). URL: https://www.researchgate.net/publication/263601538_Political_Discourse_Analysis_Exploring_the_Language_of_Politics_and_the_Politics_of_Language/link/5b43617faca2728a0d662fdc/download?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InB1YmxpY2F0aW9uIn19