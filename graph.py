# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# Ian Snyder

import functools

class Graph:

    def __init__(self):
        self.data = {}

    def adjacent(self, v1, v2):
        if len(self.data) <= 1:
            return False
        else:
            return True

    def neighbors(self, vertex):
        if len(self.data) <= 1:
            return []
        else:
            return -1

    def add_vertex(self, vertex):
        if self.contains_vertex(vertex) == False:
            self.data.update({vertex: []})
        else:
            return -1
            
    def contains_vertex(self, vertex):
        contains_vertex = False
        for x in self.data.keys():
            if x == vertex:
                contains_vertex == True
            else:
                return contains_vertex

    def remove_vertex(self, vertex):
        pass

    def add_edge(self, v1, v2):
        pass

    def remove_edge(self, v1, v2):
        pass



