by Illarionov Alexei, Bolotova Ekaterina, GitHub
## Key idea of project

The main idea of the current project is to calculate the city and university based on user groups. We have two ideas for calculating the data:

1. Set the central groups manually and go from them. That is, we identify those groups that, with a relatively high probability, may indicate that the user belongs to a particular city/university. Next, we collect user groups and find intersections, thereby defining a set of groups, participation in which increases the likelihood that the user belongs to a particular city/university.

2. Find the group data automatically by determining the concentration of users with a particular profile characteristic in the group. And then, after determining the main groups, go further along the first step.

Next, it is planned to compare the results obtained. We can also compare it with real user data (despite the fact that this information is not recorded at all, we can find out from a sufficient number of users) In fact, this approach is just an example that can be reused for other tasks, for example, to determine which political force the current user belongs to or which genre of music he prefers, and so on.

## Dataset required to do the project

To implement the current work, it is necessary to obtain:

1. Data from the list of groups that belong to a certain category.

2. Data of the group members.

3. Data about the groups of a particular user.

All this data can be obtained using the VK api for developers and a program that will call this API and write the results to the database.

## Anticipated SNA Methods

1. Community Detection
2. Centrality Analysis
3. Graph network analysis / graph convolutional networks / graph attention networks
4. User profiling