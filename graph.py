from collections import namedtuple

Vertex = namedtuple('Vertex', ['vertex', 'value'])
Edge = namedtuple('Edge', ['edge', 'value'])

class Graph:
    def __init__(self):
        self.number_of_teams = 50
        self.number_of_vertices = 0
        self.number_of_edges = 0
        self.vertices = []
        self.edges = [[0 for x in range(self.number_of_teams)] for y in range(self.number_of_teams)]
        for i in range(self.number_of_teams):
            for j in range(self.number_of_teams):
                self.edges[i][j] = Vertex(".", 0)

    def add_vertex(self, new_vertex: str) -> None:
        self.vertices.append(Vertex(new_vertex, "-1"))
        self.number_of_vertices = self.number_of_vertices + 1

    def add_edge(self, vertex1: str, vertex2: str) -> None:
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)
        if v1 == -1 or v2 == -1:
            print("Incorrect vertices")
            return
        self.edges[v1][v2].edge = "1"
        self.edges[v2][v1].edge = "1"
        self.number_of_edges = self.number_of_edges + 1

    def find_vertex(self, vertex: str) -> int:
        for v in range(self.number_of_vertices):
            if self.vertices[v].vertex == vertex:
                return v
        return -1

    def set_vertex_value(self, vertex: str, value: int) -> None:
        v = self.find_vertex(vertex)
        if v == -1:
            print(f"There is no vertex {vertex}")
            return
        self.vertices[v] = Vertex(vertex, value)

    def get_vertex_value(self, vertex: str) -> int:
        v = self.find_vertex(vertex)
        if v != -1:
            return self.vertices[v].value
        print(f"There is no vertex {vertex}")
        return -1111111

    # are neighbours?
    def adjacent(self, vertex1: str, vertex2: str) -> bool:
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)
        if v1 == -1 or v2 == -1:
            print("Incorrect vertices")
            return False
        if self.edges[v1][v2].edge == ".":
            return False
        return True

    def set_edge_value(self, vertex1: str, vertex2: str, value: int) -> None:
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)
        if v1 == -1 or v2 == -1:
            print("Incorrect vertices")
            return
        self.edges[v1][v2].value = value
        self.edges[v2][v1].value = value

    
    # n - number of teams
    # names - names of teams
    def create_graph(self, n: int, names: list):

        graph = Graph()
        tmp = ''
        value = 0

        for i in range(n-1):
            for j in range(n-1):
                tmp = names[i] + ' - ' + names[j]
                graph.add_vertex(tmp)
                graph.set_vertex_value(tmp, value)
                value = value + 1

        first_team = ''
        second_team = ''
        new_team = ''
        value = 0
        index = 0
        index2 = 0

        for i in range(self.number_of_vertices):
            index = graph.vertices[i].find(" ")
            first_team = graph.vertices[i].vertex[0:index]
            new_team = graph.vertices[i].vertex[index+3:]
            for j in range(self.number_of_vertices):
                if i == j:
                    continue
                second_team = (graph.vertices[j].vertex)[0:index]
                if(first_team == second_team or new_team == second_team):
                    graph.add_edge(graph.vertices[i].vertex, graph.vertices[j].vertex)
                else:
                    index2 = (graph.vertices[j].vertex).find(" ")
                    second_team = (graph.vertices[j].vertex)[index2+3:]
                    if(first_team == second_team or new_team == second_team):
                        graph.add_edge(graph.vertices[i].vertex, graph.vertices[j].vertex)

        return graph

                

    def color_the_graph(self):
        n = self.number_of_vertices
        CT = []     # list of colors
        C = []      # list of bool's
        i = 0
        v = 0

        for i in range (n):
            CT[i] = -1

        CT[0] = 0   # first vertex's color 

        for v in range (1, n):
            for i in range(n):
                C[i] = False
            for j in range (n):
                if self.adjacent(self.vertices[v].vertex, self.vertices[j].vertex):
                    if CT[self.vertices[j].value] > -1:
                        C[CT[self.vertices[j].value]] = True
            for i in range (n):
                if C[i]:
                    break
            CT[v] = i

        max = CT[0]
        for s in range (1, n):
            if max < CT[s]:
                max = CT[s]

        for v in range (max+1):
            print(f"Runda {v+1}: ")
            for k in range (n):
                if v != CT[k]:
                    continue
                print(f"{self.vertices[k].vertex}")




