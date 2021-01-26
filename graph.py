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
                self.edges[i][j] = Edge(".", 0)

    def add_vertex(self, new_vertex: str) -> None:
        self.vertices.append(Vertex(new_vertex, "-1"))
        self.number_of_vertices = self.number_of_vertices + 1

    def add_edge(self, vertex1: str, vertex2: str) -> None:
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)
        if v1 == -1 or v2 == -1:
            print("Incorrect vertices")
            return
        tmp = self.edges[v1][v2].value
        self.edges[v1][v2] = Edge("1", tmp)
        self.edges[v2][v1] = Edge("1", tmp)
        # self.edges[v1][v2].edge = "1"
        # self.edges[v2][v1].edge = "1"
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

    
    # names - names of teams
    def create_graph(self, names: list):

        # number of teams
        n = len(names)        
        graph = Graph()
        tmp = ''
        value = 0

        for i in range(n-1):
            for j in range(i+1,n):
                tmp = names[i] + ' - ' + names[j]
                graph.add_vertex(tmp)
                graph.set_vertex_value(tmp, value)
                value = value + 1

        left_team = ''
        right_team = ''
        next_left_team = ''
        next_right_team = ''
        value = 0
        first_match_index = 0
        second_match_index = 0

        for i in range(graph.number_of_vertices):
            first_match_index = graph.vertices[i].vertex.find(" ")
            left_team = graph.vertices[i].vertex[0:first_match_index]
            right_team = graph.vertices[i].vertex[first_match_index+3:]
            for j in range(graph.number_of_vertices):
                if i == j:
                    continue
                second_match_index = (graph.vertices[j].vertex).find(" ")
                next_left_team = (graph.vertices[j].vertex)[0:second_match_index]
                next_right_team = (graph.vertices[j].vertex)[second_match_index+3:]
                if left_team == next_left_team or left_team == next_right_team or right_team == next_right_team or right_team == next_right_team:
                    graph.add_edge(graph.vertices[i].vertex, graph.vertices[j].vertex)

        return graph

                 

    def color_the_graph(self):
        n = self.number_of_vertices
        # list of colors
        CT = []   

        # list of bool's  
        C = []      
        i = 0
        v = 0

        for i in range (n):
            CT.append(-1)
            C.append(False)

        # first vertex's color 
        CT[0] = 0   

        for v in range (1, n):
            for i in range(n):
                C[i] = False
            for j in range(n):
                if self.adjacent(self.vertices[v].vertex, self.vertices[j].vertex):
                    if CT[self.vertices[j].value] > -1:
                        C[CT[self.vertices[j].value]] = True
            for i in range(0, n):
                if not C[i]:
                    break
            CT[v] = i

        max = CT[0]
        for s in range (1, n):
            if max < CT[s]:
                max = CT[s]

        for v in range (max+1):
            print(f"Round {v+1}: ")
            for k in range (n):
                if v != CT[k]:
                    continue
                print(f"{self.vertices[k].vertex}")




