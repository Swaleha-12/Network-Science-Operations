class Edge:
    """ An undirected edge. """

    def __init__(self, v0: int, v1: int):
        """Create edge with endpoints at v0 and v1.

        Args:
        - self: the instance to create.
        - v0, v1: endpoints of the edge

        Returns:
        nothing.
        """
        self.v0, self.v1 = sorted((v0, v1))

    def __repr__(self) -> str:
        """Returns string representation of edge for printing.

        Allows `print()` on instances.

        Args:
        - self: this instance.

        Returns:
        string representation for printing.
        """
        return f'({self.v0}, {self.v1})'

    def __eq__(self, other: Edge) -> bool:
        """Does other have the same enpoints?

        Allows `==` on instances.

        Args:
        - self: this instance.
        - other: edge to compare with.

        Returns:
        True if other has the same endpoints as this edge.
        """
        if type(other) == type(self):
            return self.v0, self.v1 == other.v0, other.v1
        return False

    def __hash__(self) -> int:
        """Returns hash of this edge.

        Makes instances hashable, allows adding them to appropraite containers,
        e.g. `set`, `dict`.

        Args:
        - self: this instance.

        Returns:
        a hash of this edge.

        """
        return hash(tuple(sorted(self.__dict__.items())))

    def __contains__(self, v) -> bool:
        """Is v an endpoint of this edge?

        Allows `in` syntax.

        Args:
        - self: this instance.
        - v: the vertex to check.

        Returns:
        True if v is an endpoint, False otherwise.
        """
        return v == self.v0 or v == self.v1

    def nbr(self, v: int) -> int:
        """Returns the neighbor of v along this edge if v is an endpoint.

        Args:
        - self: this instance.
        - v: the vertex whose neighbor is sought.

        Returns:
        the other endpoint if v is an endpoint, otherwise None.
        """
        return self.v0 if v == self.v1 else self.v1 if v == self.v0 else None


class Graph:
    """ Represents an undirected, possibly weighted, graph. """

    def __init__(self, edges: str, imp: str):
        """Creates graph with the given edges using the specified implementation.

        edges consists of multiple lines representing an edge list
        representation of the graph. Each line contains 2 vertices and an
        optional weight. All values in a line are separated by spaces. The vertices have integer values
        and the optional weight is a float. The vertices need not begin at 0.

        the value of imp sepcifies the graph implementation to be used as follows:
        sets   : two sets, one each for the vertices and the edges
        matrix : adjacenccy matrix
        list   : adjacency list

        Args:
        self: the instance to create.
        edges: an edge list representation of the graph
        imp: the implementation to be used

        Returns:
        nothing.
        """
        if imp == "sets":
            self.graph = SetGraph(edges)
        elif imp == "matrix":
            self.graph = AdjacencyMatrix(edges)
        elif imp == "list":
            self.graph = AdjacencyList(edges)

    def vertices(self):
        """Iterates over the vertices in the graph.

        Args:
        - self: the instance to operate on.

        Returns:
        nothing.

        Yields:
        vertices in the graph.
        """
        pass

    def edges(self) -> {Edge}:
        """Iterates over the edges in the graph.

        Args:
        - self: the instance to operate on.

        Returns:
        nothing.

        Yields:
        vertices in the graph.
        """
        pass

    def vertex_count(self) -> int:
        """Returns the number of vertices in the graph.

        Args:
        - self: the instance to operate on.

        Returns:
        the number of vertices in the graph.
        """
        pass

    def edge_count(self) -> int:
        """Returns the number of edges in the graph.

        Args:
        - self: the instance to operate on.

        Returns:
        the number of edges in the graph.
        """
        pass

    def has_vertex(self, v) -> bool:
        """Returns whether v is a vertex in the graph.

        Args:
        - self: the instance to operate on.
        - v: its neighbors in the graph are to be returned.

        Returns:
        True if v is a vertex in the graph, False otherwise.
        """
        pass

    def has_edge(self, v0, v1) -> bool:
        """Returns whether the grpah contains an edge between v0 and v1.

        Args:
        - self: the instance to operate on.
        - v0, v1: does an edge exist between vertices v0 and v1 in the graph?

        Returns:
        True if an edge exists between v0 and v1 in the graph, False otherwise.
        """
        assert self.has_vertex(v0) and self.has_vertex(v1), \
            f'one or more of {v0} and {v1} are not valid vertices'
        pass

    def has_weights(self) -> bool:
        """Returns whether the graph is weighted.

        Args:
        - self: the instance to operate on.

        Returns:
        True if the graph edges are weighted, False otherwise.
        """
        pass

    def neighbors(self, v):
        """Iterates over the neighbors of the vertex v in the graph.

        Errors if v is not in the graph. Check before calling.

        Args:
        - self: the instance to operate on.
        - v: the vertex whose neighbors in the graph are sought.

        Returns:
        nothing.

        Yields:
        neighbors of v in the graph.
        """
        pass

    def degree(self, v) -> {int}:
        """Returns the degree of the vertex v in the graph.

        Errors if v is not in the graph. Check before calling.

        Args:
        - self: the instance to operate on.
        - v: its degree in the graph is to be returned.

        Returns:
        degree of v in the graph.
        """
        pass
