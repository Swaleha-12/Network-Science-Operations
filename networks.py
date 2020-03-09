import graphviz
from graphs import *


class NetworkOperations:
    def degree_centrality(self, g: Graph, vtx: int) -> float:
        """Returns the degree centrality of the vertex, vtx in the graph, g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex in g whose degree centrality is sought.

        Returns:
        the degree centrality of vtx in g.
        """

        return g.degree(vtx)/(g.vertex_count()-1)

    def local_centrality(self, g: Graph, vtx: int) -> int:
        nbr = list()
        for neighbor in g.neighbors(vtx):
            nbr.append(neighbor)
        ki = len(nbr)
        denominator = (ki*(ki-1))/2
        L = 0
        for i in nbr:
            nv = g.neighbors(i)
            for j in range(g.degree(i)):
                if nv in nbr:
                    L += 1
                nv = next(g.neighbors(i))
        if L:
            return (L//2)/denominator
        else:
            return 0

    def clustering_coefficient(self, g: Graph, vtx: int = None) -> float:
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
            return self.local_centrality(g, vtx)

        else:
            sum = 0
            for i in g.vertices():
                sum += self.local_centrality(g, i)
            return sum

    def average_neighbor_degree(self, g: Graph, vtx: int) -> float:
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

    def similarity(self, g: Graph, v0: int, v1: int) -> float:
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

    def popular_distance(self, g: Graph, vtx: int) -> int:
        """Returns the popular distance of the vertex, vtx, in g.

        Args:
        - g: the graph/network to be checked.
        - vtx: the vertex in g whose popular distance is sought.

        Returns:
        the popular distance of the vertex, vtx, in g.
        """
        # finding popular vertex first
        source, max_dist = 0, 0

        for i in g.vertices():
            if g.degree(i) > max_dist:
                source, max_dist = i, g.degree(i)

        inf = float('inf')

        # 1. Mark all nodes unvisited and store them.
        # 2. Set the distance to zero for our initial node
        # and to infinity for other nodes.
        distances = {vertex: inf for vertex in g.vertices()}
        previous_vertices = {
            vertex: None for vertex in g.vertices()
        }
        distances[source] = 0
        vertices = []
        for i in g.vertices():
            vertices.append(i)

        while vertices:
            # 3. Select the unvisited node with the smallest distance,
            # it's current node now.
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])

            # 6. Stop, if the smallest distance
            # among the unvisited nodes is infinity.
            if distances[current_vertex] == inf:
                break

            # 4. Find unvisited neighbors for the current node
            # and calculate their distances through the current node.
            for neighbour in g.neighbors(current_vertex):
                if g.weight(current_vertex, neighbour):
                    alternative_route = distances[current_vertex] + \
                        g.weight(current_vertex, neighbour)
                else:
                    alternative_route = distances[current_vertex]
                # Compare the newly calculated distance to the assigned
                # and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

            # 5. Mark the current node as visited
            # and remove it from the unvisited set.
            vertices.remove(current_vertex)

        path, current_vertex = list(), vtx
        while previous_vertices[current_vertex] is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.insert(0, current_vertex)
        return len(path)

    def visualize(self, g: Graph) -> None:
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
