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
        return self.graph.vertices()

    def edges(self) -> {Edge}:
        """Iterates over the edges in the graph.
        Args:
        - self: the instance to operate on.
        Returns:
        nothing.
        Yields:
        vertices in the graph.
        """
        return self.graph.edges()

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
        return self.graph.has_edge(v0, v1)

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
        return self.graph.neighbors(v)

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
        return self.graph.weight(v0, v1)


""" Set Graph """


class SetGraph(Graph):
    def __init__(self, edges):
        self.verset = set([]) #set of vertices
        self.edgeset = set([]) #set of edges (Edge type)
        self.weighted = False #if the graph is weighted
        self.edgeCount = 0 
        self.verCount = 0
        
        for line in edges.splitlines(): #'line' is string form of an edge
            if line != '':
                line = line.split()
                if len(line) > 2: # if the edge is weighted
                    line = [ int(line[0]), int(line[1]), eval(line[2]) ]
                    self.edgeset.add((Edge(line[0], line[1]), line[2])) # a tuple with edge and it's weight
                else: # if the graph is not weighted
                    line = [ int(line[0]), int(line[1]) ] 
                    self.edgeset.add((Edge(line[0], line[1]), 1)) # 1 is the default weight
                _line = line[:2] # eliminates the possibility of checking weight as a vertex
                for ver in _line: # an edge consists of two vertices, hence the loop
                    if ver not in self.verset:
                        self.verCount += 1 # to keep count of the number of vertices
                        self.verset.add(ver) # add vertex to the set
                self.edgeCount += 1 #number of times main loop runs the number of edges
        if len(line) > 2: # if the graph is weighted
            self.weighted = True

    def vertices(self):
        # yields vertices by iterating over the set of vetices
        for ver in self.verset:
            yield ver

    def edges(self):
        # yields edges by iterating over the set of edges
        for edge in self.edgeset:
            yield edge[0]

    def vertex_count(self) -> int:
        # returns the number of vertices
        return self.verCount

    def edge_count(self) -> int:
        #returns the number of edges
        return self.edgeCount

    def has_vertex(self, v) -> bool:
        # if v exits in set of vertices then returns true, otherwise false
        return v in self.verset

    def has_edge(self, v0, v1) -> bool:
        # if v0 exists in any edge and the other end of edge is v1 then returns true otherwise false
        for edge in self.edgeset:
            if v0 in edge[0] and edge[0].nbr(v0) == v1:
                return True
        return False

    def has_weights(self) -> bool:
        # returns True if the graph is weighted, otherwise false
        return self.weighted

    def neighbors(self, v):
        # iterates over edge and checks if v is an endpoint of an edge. if it is then yields the other endpoint
        for edge in self.edgeset:
            if v in edge[0]:
                yield edge[0].nbr(v)

    def degree(self, v) -> {int}:
        # if v is an endpoint of any edge. It's degree increments by 1
        deg = 0
        for edge in self.edgeset:
            if v in edge[0]:
                deg += 1
        return deg

    def weight(self, v0: int, v1: int):
        # if v0 is an endpoint of an edge and v1 is the other endpoint then returns the weight, otherwise returns None
        # if the graph is unweighted the default answer is also None
        if self.weighted:
            for edge in self.edgeset:
                if v0 in edge[0] and edge[0].nbr(v0) == v1:
                    return edge[1]
        return None


class AdjacencyMatrix:
    def __init__(self, edges):
        self.verdict = dict() #dictionary to map the vertices to sequential whole numbers
        self.weighted = False # whether the graph is weighted or not
        self.matrix = []
        self.verCount = 0
        self.edgeCount = 0
        lst = [] #temporary lst of 0's for matrix
        edges = edges.splitlines()
        for line in edges: # loop#1 to collect all the vertices
            if line != '':
                line = line.split()
                line = [int(line[0]), int(line[1])]
                for ver in line:
                    if ver not in self.verdict: 
                        self.verdict[ver] = self.verCount # maps vertex to a whole number
                        self.verCount += 1
                        lst.append(0) # appends 0's to the list number of vertices times
                self.edgeCount += 1  # number of times the for loop runs the number of edges
                
        for i in range(self.verCount): # appends list of 0's to the matrix number of vertices times
            self.matrix.append(list(lst)) 

        for line in edges: #loop #2 to go through the edges
            if line != '':
                line = line.split()
                if len(line) > 2: # if weighted, change the corresponding row and column value to the weight
                    line = [int(line[0]), int(line[1]), eval(line[2])]
                    self.matrix[self.verdict[line[0]]
                                ][self.verdict[line[1]]] = line[2]
                    self.matrix[self.verdict[line[1]]
                                ][self.verdict[line[0]]] = line[2]
                else: # if unweighted, change the corresponding row and column value to the 1
                    line = [int(line[0]), int(line[1])]
                    self.matrix[self.verdict[line[0]]
                                ][self.verdict[line[1]]] = 1
                    self.matrix[self.verdict[line[1]]
                                ][self.verdict[line[0]]] = 1
        if len(line) > 2:
            self.weighted = True

    def vertices(self):
        # iterates over the vertices and yields them one by one
        for key in self.verdict.keys():
            yield key

    def edges(self):
        # iterates over the entire matrix and finds non-zero values, then appends the corresponding edges
        keyList = list(self.verdict.keys()) #list of all vertices
        valueList = list(self.verdict.values()) #list of whole number mapping of the vertices
        visited = []
        for i in range(self.verCount):
            ver1 = keyList[valueList.index(i)] # gets vertex by getting the index of value list which is the same index location as the key in keylist
            for j in range(self.verCount):
                ver2 = keyList[valueList.index(j)] 
                if self.matrix[i][j] and ver2 not in visited:
                    yield Edge(ver1, ver2)
            visited.append(ver1) # keeps check of vetices whose edges have been completely traversed

    def vertex_count(self) -> int:
        # returns number of vertices
        return self.verCount

    def edge_count(self) -> int:
        #returns number of edges
        return self.edgeCount

    def has_vertex(self, v) -> bool:
        # if the vertex exists in the graph returns true otherwise false
        return v in self.verdict

    def has_edge(self, v0, v1) -> bool:
        # the corresponding row and column has a weight or 1, then return true otherwise false
        return bool(self.matrix[self.verdict[v0]][self.verdict[v1]]) == True

    def has_weights(self) -> bool:
        # returns true if the graph is weighted
        return self.weighted

    def neighbors(self, v):
        # yields the neighbors of vertex v one by one
        if self.has_vertex(v):
            keyList = list(self.verdict.keys())
            valueList = list(self.verdict.values())
            for i in range(self.verCount):
                if self.matrix[self.verdict[v]][i]:
                    yield keyList[valueList.index(i)]

    def degree(self, v) -> {int}:
        # traverses the corresponding row and increments one if a true value is encountered
        if self.has_vertex(v):
            deg = 0
            for i in self.matrix[self.verdict[v]]:
                if i:
                    deg += 1
            return deg

    def weight(self, v0: int, v1: int):
        # returns the weight of the edge
        if self.has_edge(v0, v1) and self.weighted:
            return self.matrix[self.verdict[v0]][self.verdict[v1]]
        return None


class AdjacencyList(Graph):

    def __init__(self, edges):

        self.adjList = dict()  # adjacency List representation
        self.weighted = False  # weather the graph has weights or not
        self.edgeCount = 0
        for line in edges.splitlines():
            if line != '':
                line = line.split()
                if len(line) > 2: # if weighted,then add the other end of the edge and weight as a tuple to adjacency list
                    line = [int(line[0]), int(line[1]), eval(line[2])]
                    self.adjList[line[0]] = self.adjList.get(
                        line[0], []) + [(line[1], line[2])]
                    self.adjList[line[1]] = self.adjList.get(
                        line[1], []) + [(line[0], line[2])]
                else: # if unweighted, then add 1 with the vertex as a default weight
                    line = [int(line[0]), int(line[1])]
                    self.adjList[line[0]] = self.adjList.get(
                        line[0], []) + [(line[1], 1)]
                    self.adjList[line[1]] = self.adjList.get(
                        line[1], []) + [(line[0], 1)]
                self.edgeCount += 1 # number of times main loop runs is the number of edges
        if len(line) > 2:
            self.weighted = True
        # number of keys represent the number of vertex
        self.verCount = len(self.adjList)

    def vertex_count(self):
        # returns number of vertices
        return self.verCount

    def edge_count(self):
        # returns number of edges
        return self.edgeCount

    def vertices(self):
        # yields vertices one by one
        for key in self.adjList.keys():
            yield key

    def edges(self):
        # yield edges one by one
        visited = []
        for key in self.adjList:
            for val in self.adjList[key]:
                if val[0] not in visited:
                    yield Edge(key, val[0])
            visited.append(key)

    def has_vertex(self, v):
        # returns true if the vertex exists in the graph
        return v in self.adjList

    def has_edge(self, v0, v1):
        # returns true if the edge exists in the graph
        for val in self.adjList[v0]:
            if val[0] == v1:
                return True
        return False

    def degree(self, v):
        # returns the degree of the vertex
        if self.has_vertex(v):
            return len(self.adjList[v])

    def neighbors(self, v):
        # returns neighbors of v
        if self.has_vertex(v):
            for ver in self.adjList[v]:
                yield ver[0]

    def has_weights(self):
        # returns whether the graph has is weighted or not
        return self.weighted

    def weight(self, v0, v1):
        # returns the weight of the corresponding edge between the given vertices
        if self.has_edge(v0, v1) and self.weighted:
            for val in self.adjList[v0]:
                if val[0] == v1:
                    return val[1]
        return None
