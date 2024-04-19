# File formats and graph tools

## Graph data sources classification

1. Graph Databases
    * Graph Query languages
3. Relational Databases
    * SQL
3. Files
    * Common tables
    * Specific graph formats
    * Domain-oriented formats
## File formats

### Main formats

1. [Description](http://users.cecs.anu.edu.au/~bdm/data/formats.txt) of graph6, sparse6 and digraph6 encodings
2. [DOT](https://en.wikipedia.org/wiki/Dot) (graph-description,language)
3. [GraphML](http://graphml.graphdrawing.org/specification.html)
4. [GXL](http://www.gupro.de/GXL/) (Graph eXchange Language)
5. GML (Graph Modelling Language)
    * [from yFiles](https://docs.yworks.com/yfiles/doc/developers-guide/gml.html) 
    * [from Gephi](https://gephi.org/users/supported-graph-formats/gml-format/)
## Domain specific graph formats

1. [OpenBabel](http://openbabel.org/wiki/Main_Page)
[github](https://github.com/openbabel/openbabel/), [file formats](https://github.com/openbabel/documentation/tree/master/FileFormats)

## Data collection file formats

1.UCI Network [Data Repository Download](http://networkdata.ics.uci.edu/getting_started.php) formats
a.	[Pajek](http://mrvar.fdv.uni-lj.si/pajek/)
b.	[GML](https://networkx.org/documentation/networkx-1.9/reference/readwrite.gml.html)
c.	[GraphML](http://graphml.graphdrawing.org/)
d.	[DyNetML](http://www.casos.cs.cmu.edu/projects/dynetml/)

## Main implementations
1. [graph-tool](https://graph-tool.skewed.de/)
2. [Snap](https://snap.stanford.edu/snappy/index.html) от Стенфордской группы
3. JGraphT - java библиотека с [питоновской обвязкой](https://medium.com/@dimitrios.michail/announcing-the-python-bindings-of-jgrapht-918d0cf386de).
4. [stellargraph](https://stellargraph.readthedocs.io/en/stable/) для эббеддингов
1. [NetworkX](http://networkx.org/) - a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks
* *[*Converting to and from other data formats*](http://networkx.org/documentation/stable/reference/convert.html#)
2. [ReGraph](https://cambridge-intelligence.com/regraph/) - a Python package for advanced graph visualisation
* [*ReGraph tutorial*](https://cambridge-intelligence.com/python-graph-visualization-using-jupyter-regraph/)
3. [IGraph](https://igraph.org/) - Network analysis software
* [*Reading and Writing Graphs from and to Files*](https://igraph.org/c/doc/igraph-Foreign.html)
4. [Graphviz](http://graphviz.org/) - Graph Visualization Software
* [*The DOT Language*](http://graphviz.org/doc/info/lang.html)
5. [Gephi](https://gephi.org/) - the leading visualization and exploration software for all kinds of graphs and networks
* [*Supported Graph Formats*](https://gephi.org/users/supported-graph-formats/)
6. [Cytoscape](https://cytoscape.org/) - an open source software platform for visualizing complex networks 
7. [Graphjstry](https://www.graphistry.com/) , [pygraphistry](https://github.com/graphistry/pygraphistry) - has a list of connectors
8. [NodeXL](https://www.smrfoundation.org/nodexl/) - add-in for Microsoft Excel that support social network and content analysis. Moreover, it has some build-in importers of social-web data (Flickr, Twitter, Youtube) and you are able to download additional importers.
10. [Socnetv](https://socnetv.org/): social network analysis and visualization software
* [*Supported Formats*](https://socnetv.org/docs/formats.html)
11. [vosviewer](https://www.vosviewer.com/) - a software tool for constructing and visualizing bibliometric networks
12. [CitNetExplorer](https://www.citnetexplorer.nl/) - a software tool for visualizing and analyzing citation networks of scientific publications
13. yworks [yed](https://www.yworks.com/products/yed)
    * [online demo](https://www.yworks.com/products/yfiles/demos)
14. [ogma](https://doc.linkurio.us/ogma/latest/) 
15. sigma
16. [ngraph](https://github.com/anvaka/map-of-github)
17. [forcegraph](https://github.com/vasturiano/force-graph), cool [3d viz](https://vasturiano.github.io/3d-force-graph/example/large-graph/)
18. [d3](https://d3js.org/)
19. [ibm i2](https://www.ibm.com/security/resources/demos/i2-analysts-notebook-demo/)
20. CASOS [ORA](http://www.casos.cs.cmu.edu/projects/ora/)
21. [Pajek](http://vlado.fmf.uni-lj.si/pub/networks/pajek/)
22. [neo4j](https://neo4j.com/developer/tools-graph-visualization/)

Интересное сравнение бенчмарков есть в статье [Benchmark of popular graph/network packages](https://www.timlrx.com/blog/benchmark-of-popular-graph-network-packages-v2) v2

## Publications and prototypes
1. [LargeViz](https://github.com/lferry007/LargeVis)
[github](https://github.com/elbamos/largeVis), [Visualizing Large-scale and High-dimensional Data](https://arxiv.org/abs/1602.00370)
2. [mars](https://github.com/marckhoury/mars) - a graph drawing tool for large graph visualization
3. [Interactive Graph Layout of a Million Nodes](https://www.mdpi.com/2227-9709/3/4/23/htm)

## Nice visualizations

# Graph Visualization

* [Network Repository](https://networkrepository.com/)
    * [Cora in Network Repository](https://networkrepository.com/graphvis.php?d=./data/gsm50/labeled/cora.edges)

- julesvernestrilogy.com
- [internet-map.net](http://internet-map.net) / webverse.org

* Graph visualization [хабр](https://habr.com/ru/company/ods/blog/464715/), [towardsdatascience](https://towardsdatascience.com/large-graph-visualization-tools-and-approaches-2b8758a1cd59) 
* Another visualization Deep Graph Library [блог](https://www.dgl.ai/blog/2019/02/17/gat.html)

* Хороший гайд по [yFiles Automatic Graph Layout](https://www.youtube.com/watch?v=AkR6r1FbRdY)
    * [yEd](https://www.yworks.com/yed-live/) - Live Graph Editor
    * [Layout-Styles Demo](https://live.yworks.com/demos/layout/layoutstyles/index.html) (offers more settings)

## References
* "[A survey of two-dimensional graph layout techniques for information visualisation](https://dl.dropboxusercontent.com/s/p4aoaxpyij0ml7x/1473871612455749.pdf)" [@gibsonSurveyTwodimensionalGraph2013]
* "[What Would a Graph Look Like in This Layout? A Machine Learning Approach to Large Graph Visualization](https://arxiv.org/pdf/1710.04328.pdf)" [@kwonWhatWouldGraph2018]
