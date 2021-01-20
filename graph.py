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
        for v in range(self.number_of_edges):
            if self.vertices[v].vertex == vertex:
                return v
        return -1

    def set_vertex_value(self, vertex: str, value: int) -> None:
        v = self.find_vertex(vertex)
        if v == -1:
            print(f"There is no vertex {vertex}")
            return
        self.vertices[v].value = value

    def get_vertex_value(self, vertex: str) -> int:
        v = self.find_vertex(vertex)
        if v != -1:
            return self.vertices[v].value
        print(f"There is no vertex {vertex}")
        return -1111111

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
                if(firstTeam == secondTeam or newTeam == secondTeam):
                    graph.add_edge(graph.vertices[i].vertex, graph.vertices[j].vertex)
                else:
                    index2 = (graph.vertices[j].vertex).find(" ")
                    secondTeam = (graph.vertices[j].vertex)[index2+3:]
                    if(firstTeam == secondTeam or newTeam == secondTeam):
                        graph.addEdge(graph.vertices[i].vertex, graph.vertices[j].vertex)

                

