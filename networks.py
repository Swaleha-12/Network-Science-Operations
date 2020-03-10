import graphviz
from graphs import *
import math


def local_centrality(g: Graph, vtx: int) -> int:
    nbr = list()
    L = 0
    ki = 0
    for n in g.neighbors(vtx):
        for n_of_n in g.neighbors(vtx):
            if n == n_of_n:
                continue
            else:
                if n_of_n in nbr:
                    continue
                elif n_of_n in g.neighbors(n):
                    L += 1

        ki += 1
        nbr.append(n)
    if ki == 1:
        return 0
    return (L / ((ki*(ki-1))/2))


def dijkstra(g: Graph, src, dst=None):
    nodes = []
    for n in g.vertices():
        nodes.append(n)
        nodes += [x for x in g.neighbors(n)]
    q = set(nodes)
    nodes = list(q)
    dist = dict()
    for n in nodes:
        dist[n] = float('inf')
    dist[src] = 0
    count = 0
    while q:
        u = min(q, key=dist.get)
        q.remove(u)
        if dst is not None and u == dst:
            if dist[dst] == math.inf:
                return -1
            return dist[dst]
        for v in g.neighbors(u):
            w = g.weight(u, v)
            if w == None:
                w = 1
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
        count += 1
    return dist


class NetworkOperations:
    def degree_centrality(g: Graph, vtx: int) -> float:
        """Returns the degree centrality of the vertex, vtx in the graph, g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex in g whose degree centrality is sought.

        Returns:
        the degree centrality of vtx in g.
        """

        return g.degree(vtx)/(g.vertex_count()-1)

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
        if vtx != None:
            return local_centrality(g, vtx)

        else:
            sum = 0
            for i in g.vertices():
                sum += local_centrality(g, i)
            return sum//g.vertices()

    def average_neighbor_degree(g: Graph, vtx: int) -> float:
        """Returns the average neighbor degree of vertex vtx in g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex whose average neighbor degree is sought.

        Returns:
        the average neighbor degree of vtx in g.
        """
        nbr = list()
        for neighbor in g.neighbors(vtx):
            nbr.append(neighbor)
        Ni = len(nbr)
        sum = 0
        for j in nbr:
            sum += g.degree(j)
        return sum/Ni

    def similarity(g: Graph, v0: int, v1: int) -> float:
        """Returns the Jaccard similarity of vertices, v0 and v1, in g.

        Args:
        - g: the graph/network to be checked.
        - v0, v1: the vertices in g who similarity is sought.

        Returns:
        The Jaccard similarity of vertices, v0 and v1, in g.
        """
        nbr = list()
        for neighbor in g.neighbors(v0):
            nbr.append(neighbor)
        nbr1 = list()
        for neighbor in g.neighbors(v1):
            nbr1.append(neighbor)
        ni, nj = len(nbr), len(nbr1)
        intersection = 0
        for i in nbr:
            if i in nbr1:
                intersection += 1
        return intersection/(ni+nj-intersection)

    def popular_distance(g: Graph, vtx: int) -> int:
        """Returns the popular distance of the vertex, vtx, in g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex in g whose popular distance is sought.

        Returns:
        the popular distance of the vertex, vtx, in g.
        """
        # finding popular vertex first
        max_dist, source = 0, vtx

        for i in g.vertices():
            deg = d.degree(i)
            if deg > max_dist:
                max_dist, source = deg, i

        return dijkstra(g, vtx, source)

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


'''graph = Graph(open("karate.txt").read(), "list")
nice = NetworkOperations().clustering_coefficient(graph, 12)
print(nice)'''
