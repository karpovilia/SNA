by Artyom Rozhkov
[https://github.com/artjop/sna-cp](https://github.com/artjop/sna-cp)

# Description (CP)
## Key Idea
- Try to analyze an text comments to find an object and evaluate their sentiment
- Created a bipartite graph with users, their objects, and their attitudes as nodes. The weight of each edge will indicate the tone of this attitude.
- Try to categorize users based on their unique attitude set.
## Limitation 
• Data Sampling Size: 20 only the first 20 posts
• Geography: only global Moscow groups
• Data Source: VK as most popular service only

## Description of the research dataset
• Table with 13887 filtered rows and 9046 not-unique ids from 300 groups • Scrapped by VK API
![](Pasted%20image%2020240516154548.png)
