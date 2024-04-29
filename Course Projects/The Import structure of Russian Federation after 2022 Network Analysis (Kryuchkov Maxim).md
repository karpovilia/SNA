
# Link to GitHub The Import structure of Russian Federation after 2022 Network Analysis (Kryuchkov Maxim)

GitHub

# Description (CP)

Since the February of 2022 Russian Government faced with serious problems with serious economic sanction. Despite the disconnect from swift and freezing of bank assets most of international companies decided to leave the Russian market till better times or sell its actives to Russian owners. In theory, most of the Russian population should have lost access to several goods and brands: clothes, cars, fizzy drinks, chocolate and etc. In fact, in spite goods inflation Russian residents still have access to it.

It is not needed to provide serious analysis to say that answer is parallel import[[1]](#_ftn1). The technology is pretty simple – the goods are bought by countries who did not spoil their relations with eastern countries and still have serious economic ties with Russia and then being re-exported to Russia.

The main idea us to understand how our import structure has changed since February of 2022 in comparasent with 2014 – «The Russian spring» and accession of The Crimea as aftermath - and 2021, the year when nobody expected so rapid escalation of conflict.

The change of import structure will help us to understand which countries has become the biggest partners at parallel import. Moreover, it will help us to understand witch western countries import goods to our economic allies. It will help us to identify the ties between countries for optimization of logistic chains and reduction transport costs.

As for SNA implementation, I am going to use directional-weighted graph described by Turkey researchers[[2]](#_ftn2).  The countries are nodes and import flow edges. As each nations import flow is not reciprocal the connections will be directed and weighted. I will cluster the countries and use community analysis. By measuring the modularity I expect to find communities among countries and identify to witch community Russia is affiliated.

It should be noted that novelty of the study is pretty decent as nobody yet tried to identify Russian import structure after changed relations with countries of Europe and USA. However, the methods used in a study are not new for international trade measuring.

Data mining is significant limitation as it not expected to find prepared dataset for chosen topic. For now it is expected to obtain data from Trademap cite (trademap.org) and modify it to suit my research design and methods.

By comparasing data between 2014, 2021 and 2023 It is hoped to see how different structure has changed and how Russian and witch niche the Russia has changed under current conditions.

  

---

[[1]](#_ftnref1) Russia adding IKEA, Lancome and other luxury goods to parallel import list. https://www.reuters.com/business/retail-consumer/russia-adding-ikea-lancome-other-luxury-goods-parallel-import-list-2023-03-13/

[[2]](#_ftnref2) Gönçer-Demiral, D., & İnce-Yenilmez, M. (2022). Network analysis of International Export Pattern. _Social Network Analysis and Mining_, _12_(1). https://doi.org/10.1007/s13278-022-00984-8

