from collections import deque
import operator


class Vertex:
    def __init__(self, vertex_name, weight=None, visited=False):
        self.vertex_name = vertex_name
        self.weight = weight
        self.visited = visited

    def __repr__(self):
        return "Vertex %s" % self.vertex_name

    def __eq__(self, obj):
        return self.vertex_name == obj.vertex_name

    def __hash__(self):
        return hash(self.vertex_name)

    def getVertex(self):
        return self.vertex_name

    def getWeight(self):
        return self.weight

    def isVisited(self):
        return self.visited

    def setVertex(self, vertex):
        self.vertex_name = vertex

    def setWeight(self, weight):
        self.weight = weight

    def setVisited(self, visited):
        self.visited = visited

        
class Edge:
    def __init__(self, source_vertex, destination_vertex, weight=1, visited=False):
        self.source = source_vertex
        self.destination = destination_vertex
        self.weight = weight
        self.visited = visited

    def __repr__(self):
        return "Edge (%s, %s) weight: %s" %(self.source, self.destination, self.weight)

    def __eq__(self, obj):
        return self.weight == obj.weight and self.source == obj.source and self.destination == obj.destination

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.destination

    def getWeight(self):
        return self.weight

    def isVisited(self):
        return self.visited

    def setSource(self, source):
        self.source = source

    def setDestination(self, destination):
        self.destination = destination

    def setWeight(self, weight):
        self.weight = weight

    def setVisited(self, visited):
        self.visited = visited


class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = edges
        self.visited = []
        self.stack = []

    def kruskals_algorithm(self):
        path = []
        sorted_edges = self.getSortedEdges()
        while len(path) != len(self.vertices) -1:
            for edge in sorted_edges:
                if self.doesNotCreateCycle(path, edge):
                    path.append(edge)
                    sorted_edges.remove(edge)
        return path

    def doesNotCreateCycle(self, path, edge):
        for edge_in_path in path:
            destination_vertex = edge_in_path.getDestination()
            destination_vertex.setVisited(True)
            if destination_vertex == edge.getDestination():
                return False
        return True

    def allNodesVisited(self):
        for vertex in self.vertices:
            if not vertex.isVisited():
                return False
        return True

    def bfs(self, start):
        self.stack.append(start)
        self.visited.append(start)
        while (len(self.stack) != 0):
            vertex = self.stack.pop()
            for adj_vertex in self.get_adjacent_vertices(vertex):
                if adj_vertex not in self.visited:
                    self.stack.append(adj_vertex)
                    self.visited.append(adj_vertex)
        return self.visited

    def getEdgeWeight(self, source, destination):
        for edge in self.edges:
            if edge.getSource() == source and edge.getDestination() == destination:
                return edge.getWeight()

    def dfs(self, vertex):
        adjacent_vertices = self.get_adjacent_vertices(vertex)
        if adjacent_vertices < self.visited:
            return None
        else:
            self.visited.append(vertex)
            for adjacent_vertex in adjacent_vertices:
                if adjacent_vertex not in self.visited:
                    self.dfs(adjacent_vertex)
            return self.visited

    def prims_algorithm(self, vertex):
        path = []
        while len(path) != len(self.vertices) -1:
            edge = self.getLowestWeightEdge(vertex, path)
            path.append(edge)
            vertex = edge.getDestination()
        return path

    def getLowestWeightEdge(self, vertex, path):
        adjacent_edges = self.get_adjacent_edges(vertex)
        lowest_weight_edge = Edge(Vertex('X'), Vertex('X'), 9999)
        visited_nodes = self.get_visited_nodes_from_edges(path)
        for edge in adjacent_edges:
            if edge.getDestination() not in visited_nodes:
                if edge.getWeight() < lowest_weight_edge.getWeight():
                    lowest_weight_edge = edge
        return lowest_weight_edge

    def get_visited_nodes_from_edges(self, path):
        visited_nodes = set()
        for edge in path:
            visited_nodes.add(edge.getDestination())
            visited_nodes.add(edge.getSource())
        return visited_nodes

    def get_adjacent_edges(self, vertex):
        adjacent_edges = []        
        for edge in self.edges:
            if edge.getSource() == vertex:
                adjacent_edges.append(edge)
        return adjacent_edges

    def find_shortest_path(self, start_vertex, end_vertex):
        distances, prev = self.djisktra(start_vertex) 
        path = []
        vertex = end_vertex
        path.append(vertex)
        while (vertex != start_vertex):
            vertex = prev[vertex]
            path.append(vertex)
        path.reverse()
        return path

    def djisktra(self, start_vertex):
        """TODO: Currently only works on undirected graphs, need to add in directed graph functionality too"""
        queue = deque([])
        distances = {}
        prev = {}
        for vertex in self.vertices:
            distances[vertex] = 99999
        queue.append(start_vertex)
        distances[start_vertex] = 0
        while len(queue) > 0:
            vertex = queue.popleft()
            for adj_vertex  in self.get_adjacent_vertices(vertex):
                if distances[adj_vertex] > distances[vertex] +self.getEdgeWeight(adj_vertex, vertex):
                    distances[adj_vertex] = distances[vertex] + self.getEdgeWeight(adj_vertex, vertex)
                    prev[adj_vertex] = vertex
                    queue.append(adj_vertex)
        return distances, prev

    def get_adjacent_vertices(self, vertex):
        adjacent_vertices = []
        for edge in self.edges:
            if edge.getDestination() == vertex:
                adjacent_vertices.append(edge.getSource())
            elif edge.getSource() == vertex:
                adjacent_vertices.append(edge.getDestination())
        return set(adjacent_vertices)

    def getSortedEdges(self):
        sorted_edges = sorted(self.edges, key=operator.attrgetter('weight'))
        return sorted_edges

    def getVertices(self):
        return self.vertices
