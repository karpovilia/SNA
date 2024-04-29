# Link to GitHub Predicting the Popularity of Spotify Playlists based on Songs and Artists (Bazhutin Anton, Pakhomov German)

GitHub

# Description (CP)

**Key Idea of Project

The goal of this project is to develop a predictive model that can forecast the popularity of Spotify playlists based on the songs and artists featured within them. This endeavor is worth pursuing due to the growing importance of playlists as a means of music discovery and consumption on streaming platforms like Spotify. By predicting the popularity of playlists, we can provide valuable insights to playlist curators, music marketers, and artists themselves, helping them optimize their content and promotional strategies to reach a wider audience.

While various studies have explored music popularity prediction and recommendation systems[ 2, 3 ], few have specifically targeted playlist popularity prediction based on the content of playlists on platforms like Spotify. However, existing research in music recommendation systems and social network analysis (SNA) can provide valuable insights and methodologies for this project.

**Who did something similar before?

In 2018 Ching-Wei Chen, Paul Lamere, Markus Schedl, Hamed Zamani published the study “Recsys challenge 2018: automatic music playlist continuation” [1]. The ACM Recommender Systems Challenge 2018 focused on automatic music playlist continuation, which is a form of the more general task of sequential recommendation. Given a playlist of arbitrary length, the challenge was to recommend up to 500 tracks that fit the target characteristics of the original playlist.

**How are we going to reach the goal?

Based on the “Spotify Million Playlist Dataset Challenge” [4], we are going to build a graph of playlists. Playlist is the graph vertex and edges - the number of matching songs and artists. The graph will help us both visualize the data and determine the impact of the artist and song on the popularity of the playlist

**Dataset Required to do the project

For this project, we will require access to a comprehensive dataset of Spotify playlists, including information such as playlist name, tracklist (songs, albums and artists), number of followers, and other relevant metadata, such as track duration. The playlist dataset “Spotify Million Playlist Dataset challenge” collected by the Spotify team in 2018 was used as a source of data.

**Anticipated SNA Methods

Social Network Analysis (SNA) methods will play a crucial role in this project, particularly in analyzing the relationships between songs, artists, and playlists within the Spotify ecosystem. Some anticipated SNA methods include:

1. Network analysis of co-occurrence: Analyzing the co-occurrence of songs and artists within playlists to uncover patterns of association and influence.
2. Centrality measures: Calculating centrality metrics to identify key songs or artists that exert significant influence on playlist popularity.
3. Community detection: Identifying clusters or communities of songs and artists within playlists to understand the structural organization of the Spotify music network.

These SNA methods will complement traditional machine learning approaches and help uncover deeper insights into the dynamics of playlist popularity on Spotify.

**References

1. C.W. Chen, P. Lamere, M. Schedl, and H. Zamani. Recsys Challenge 2018: Automatic Music Playlist Continuation. In Proceedings of the 12th ACM Conference on Recommender Systems (RecSys ’18), 2018.
2. Millecamp, M., Htun, N. N., Jin, Y., & Verbert, K. (2018, July). Controlling spotify recommendations: effects of personal characteristics on music recommender user interfaces. In _Proceedings of the 26th Conference on user modeling, adaptation and personalization_ (pp. 101-109).
3. Werner, A. (2020). Organizing music, organizing gender: algorithmic culture and Spotify recommendations. _Popular Communication_, _18_(1), 78-90.
4. https://www.aicrowd.com