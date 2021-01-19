from collections import namedtuple

Vertex = namedtuple('Vertex', ['vertex', 'value'])
Edge = namedtuple('Edge', ['edge', 'value'])

class Graph:
    def __init__(self, number_of_teams):
        self.number_of_teams = number_of_teams
        self.number_of_vertices = 0
        self.number_of_edges = 0
        self.vertices = []
        self.edges = [[0 for x in range(self.number_of_teams)] for y in range(self.number_of_teams)]
        for i in range(self.number_of_teams):
            for j in range(self.number_of_teams):
                self.edges[i][j] = Vertex(".", 0)

    def add_vertex(self, new_vertex) -> None:
        self.vertices.append(Vertex(new_vertex, "-1"))
        self.number_of_vertices = self.number_of_vertices + 1

    def add_edge(self, vertex1, vertex2) -> None:
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)
        if v1 == -1 or v2 == -1:
            print("No vertex!")
            return
        self.edges[v1][v2].edge = "1"
        self.edges[v2][v1].edge = "1"
        self.number_of_edges = self.number_of_edges + 1

    def find_vertex(self, vertex):
        for v in range(self.number_of_edges):
            if self.vertices

    


