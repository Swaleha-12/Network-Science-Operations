import graphviz
from graphs import *


class NetworkOperations:
    def degree_centrality(g: Graph, vtx: int) -> float:
        """Returns the degree centrality of the vertex, vtx in the graph, g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex in g whose degree centrality is sought.

        Returns:
        the degree centrality of vtx in g.
        """
        pass

    def clustering_coefficient(g: Graph, vtx: int = None) -> float:
        """Returns the local or average clustering coefficient in g depending on vtx.

        vtx = None : average clustering coefficient of g
        vtx != None : local clustering coefficient of vtx in g

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex at which local clustering coefficient is sought.

        Returns:
        the local or average clustering coefficient in g.
        """
        pass

    def average_neighbor_degree(g: Graph, vtx: int) -> float:
        """Returns the average neighbor degree of vertex vtx in g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex whose average neighbor degree is sought.

        Returns:
        the average neighbor degree of vtx in g.
        """
        pass

    def similarity(g: Graph, v0: int, v1: int) -> float:
        """Returns the Jaccard similarity of vertices, v0 and v1, in g.

        Args:
        - g: the graph/network to be checked.
        - v0, v1: the vertices in g who similarity is sought.

        Returns:
        The Jaccard similarity of vertices, v0 and v1, in g.
        """
        pass

    def popular_distance(g: Graph, vtx: int) -> int:
        """Returns the popular distance of the vertex, vtx, in g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex in g whose popular distance is sought.

        Returns:
        the popular distance of the vertex, vtx, in g.
        """
        pass

    def visualize(g: Graph) -> None:
        """Visualizes g.

        Args:
        - g: the graph/network to be visualized.

        Returns:
        Nothing.
        """
        # Feel free to play around with the visualization.
        # Graphviz documentation: https://www.graphviz.org
        layout_engine = 'fdp' if g.vertex_count() < 2000 else 'sfdp'
        # graph to be visualized
        vizgraph = graphviz.Graph(engine=layout_engine)
        _ = [vizgraph.node(str(v)) for v in g.vertices()]
        vizgraph.edges(map(lambda e: (str(e.v0), str(e.v1)), g.edges()))
        vizgraph.render(view=True)
