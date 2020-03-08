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

    def __eq__(self, other) -> bool:
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
        # if imp == "sets":
        #     self.graph = SetGraph(edges)
        if imp == "matrix":
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
        for ver in self.graph.getvertices():
          yield ver

    def edges(self) -> {Edge}:
        """Iterates over the edges in the graph.

        Args:
        - self: the instance to operate on.

        Returns:
        nothing.

        Yields:
        vertices in the graph.
        """
        for edge in self.graph.getEdges():
          yield edge

    def vertex_count(self) -> int:
        """Returns the number of vertices in the graph.

        Args:
        - self: the instance to operate on.

        Returns:
        the number of vertices in the graph.
        """
        return self.graph.vertex_count()

    def edge_count(self) -> int:
        """Returns the number of edges in the graph.

        Args:
        - self: the instance to operate on.

        Returns:
        the number of edges in the graph.
        """
        return self.graph.edge_count()

    def has_vertex(self, v) -> bool:
        """Returns whether v is a vertex in the graph.

        Args:
        - self: the instance to operate on.
        - v: its neighbors in the graph are to be returned.

        Returns:
        True if v is a vertex in the graph, False otherwise.
        """
        return self.graph.has_vertex(v)

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
        return self.graph.has_edge(v0,v1)

    def has_weights(self) -> bool:
        """Returns whether the graph is weighted.

        Args:
        - self: the instance to operate on.

        Returns:
        True if the graph edges are weighted, False otherwise.
        """
        return self.graph.has_weights()

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
        for neighbor in self.graph.neighbors(v):
          yield neighbor

    def degree(self, v) -> {int}:
        """Returns the degree of the vertex v in the graph.

        Errors if v is not in the graph. Check before calling.

        Args:
        - self: the instance to operate on.
        - v: its degree in the graph is to be returned.

        Returns:
        degree of v in the graph.
        """
        return self.graph.degree(v)
    def weight(self, v0: int, v1: int):
        """Returns the weight of the edge between v0 and v1; None if no weight.

        Assumes the presence of the edge between v0 and v1. Check before calling.

        Args:
        - self: the instance to operate on.
        - v0, v1: the weight of the edge between v0 and v1 is sought.

        Returns:
        The weight of the edge between v0 and v1; None if graph is unweighted.
        """
        return self.graph.weight(v0,v1)

# class AdjacencyMatrix:
#   def __init__(self, edges):
#     f = open(edges,"r")
#     line = f.readline()
#     while line:
#       line = line.split()


class AdjacencyList(Graph):

  def __init__(self, edges):
    self.adjList = dict() #adjacency List representation
    self.weighted = False #weather the graph has weights or not
    edj = 0
    for line in edges:
      line = line.split()
      if len(line) > 2:
        line = [int(line[0]), int(line[1]), eval(line[2])]
        self.adjList[line[0]] = self.adjList.get(line[0], []) + [(line[1], line[2])]
        self.adjList[line[1]] = self.adjList.get(line[1], []) + [(line[0],line[2])]
      else:
        line = [int(line[0]),int(line[1])]
        self.adjList[line[0]] = self.adjList.get(line[0], []) + [(line[1],1)]
        self.adjList[line[1]] = self.adjList.get(line[1], []) + [(line[0],1)]
      edj+=1
    self.verCount = len(self.adjList) #number of keys represent the number of vertex
    self.edgeCount = edj

  def vertex_count(self):
    return self.verCount

  def edge_count(self):
    return self.edgeCount

  def getvertices(self) -> [int]:
    lst = []
    for key in self.adjList.keys():
      lst.append(int(key))
    return lst
  
  def getEdges(self):
    visited = []
    final = []
    for key in self.adjList:
      for val in self.adjList[key]:
        if val[0] not in visited:
          ed = Edge(key,val[0])
          final.append(ed)
      visited.append(key)
    return final

  def has_vertex(self,v):
    return v in self.adjList
  
  def has_edge(self,v0,v1):
    for val in self.adjList[v0]:
      if val[0] == v1:
        return True
    return False

  def degree(self, v):
    if self.has_vertex(v):
      return len(self.adjList[v])

  def neighbors(self, v):
    if self.has_vertex(v):
      lst = []
      for ver in self.adjList[v]:
        lst.append(ver[0])
      return lst
  
  def has_weights(self):
    return self.weighted
  
  def weight(self,v0, v1):
    if self.has_edge(v0,v1) and self.weighted:
      for val in self.adjList[v0]:
        if val[0] == v1:
          return val[1]
    return None

f = open("karate.txt")
graph = Graph(f.readlines(), "list")
print(graph.vertex_count())
