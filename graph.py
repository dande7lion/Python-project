from collections import namedtuple
from datetime import date, timedelta

# Both the vertex and the edge have a name and value
Vertex = namedtuple('Vertex', ['vertex', 'value'])
Edge = namedtuple('Edge', ['edge', 'value'])

class Graph:
    def __init__(self, number_of_teams = 50):
        self.number_of_teams = number_of_teams
        self.number_of_vertices = 0
        self.number_of_edges = 0
        self.vertices = []
        self.edges = [[0 for x in range(self.number_of_teams)] for y in range(self.number_of_teams)]
        for i in range(self.number_of_teams):
            for j in range(self.number_of_teams):
                self.edges[i][j] = Edge(".", 0)
        self.first_match_year = ""
        self.first_match_month = ""
        self.first_match_day = ""
        self.date_list = []

    def add_vertex(self, new_vertex: str) -> None:
        """ Add a new vertex to the existing graph """
        # while creating a new vertex, we give it default value, which is -1
        self.vertices.append(Vertex(new_vertex, "-1"))
        self.number_of_vertices = self.number_of_vertices + 1

    def add_edge(self, vertex1: str, vertex2: str) -> None:
        """ Add edge between two existing vertices """
        self.change_edge(vertex1, vertex2, "1")
        self.number_of_edges = self.number_of_edges + 1

    def remove_edge(self, vertex1: str, vertex2:str) -> None:
        """ Remove edge between vertex1 and vertex2 """
        self.change_edge(vertex1, vertex2, ".")
        self.number_of_edges = self.number_of_edges - 1

    def change_edge(self, vertex1: str, vertex2:str, change: str) -> None:
        """ Change edge value """
        # firstly, we have to find specific vertices
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)
        # when no vertex was found:
        if v1 == -1 or v2 == -1:
            print("Incorrect vertices")
            return
        tmp = self.edges[v1][v2].value
        # value "1" means that there is a edge between v1 and v2
        self.edges[v1][v2] = Edge(change, tmp)
        self.edges[v2][v1] = Edge(change, tmp)

    def find_vertex(self, vertex: str) -> int:
        """ Find vertex in the graph or return -1 if it does not exist """
        for v in range(self.number_of_vertices):
            if self.vertices[v].vertex == vertex:
                return v
        return -1

    def set_vertex_value(self, vertex: str, value: int) -> None:
        """ Set the value of the existing vertex """
        v = self.find_vertex(vertex)
        if v == -1:
            print(f"There is no vertex {vertex}")
            return
        self.vertices[v] = Vertex(vertex, value)

    def get_vertex_value(self, vertex: str) -> int:
        """ Give th vertex name, and get its value """
        v = self.find_vertex(vertex)
        if v != -1:
            return self.vertices[v].value
        print(f"There is no vertex {vertex}")
        return -1111111

    def adjacent(self, vertex1: str, vertex2: str) -> bool:
        """ Check if there is an edge between vertex1 and vertex2 """
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)
        if v1 == -1 or v2 == -1:
            print("Incorrect vertices")
            return False
        if self.edges[v1][v2].edge == ".":
            return False
        return True

    def set_edge_value(self, vertex1: str, vertex2: str, value: int) -> None:
        """ Set the value of the existing edge """
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
        # in tmp we'll have the vertices' names
        tmp = ''
        # in value - vertices' values
        value = 0

        for i in range(n-1):
            for j in range(i+1,n):
                # prepare vertex name
                tmp = names[i] + ' - ' + names[j]
                graph.add_vertex(tmp)
                graph.set_vertex_value(tmp, value)
                # each vertex has different value - it will be needed in color_the_graph function
                value = value + 1

        # vertex's name looks like - 'A - B' - A is the left_team, B is the right_team
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
                # we need to add edges between vertices that can not be played at one round
                if left_team == next_left_team or left_team == next_right_team or right_team == next_right_team or right_team == next_right_team:
                    graph.add_edge(graph.vertices[i].vertex, graph.vertices[j].vertex)

        return graph

                 

    def color_the_graph(self) -> None:
        """ Color the graph alghoritm """
        n = self.number_of_vertices
        # list of colors
        CT = []   

        # list of used colors (by neighbors)
        C = []      
        i = 0
        v = 0

        for i in range (n):
            CT.append(-1)
            C.append(False)

        # first vertex's color 
        CT[0] = 0   

        for v in range (1, n):
            # we reset the list of used colors
            for i in range(n):
                C[i] = False
            for j in range(n):
                # we check if two vertex are neighbor
                if self.adjacent(self.vertices[v].vertex, self.vertices[j].vertex):
                    # and if our current's vertex neighbor already has a color, we have to mark its color like used
                    if CT[self.vertices[j].value] > -1:
                        C[CT[self.vertices[j].value]] = True
            # we're looking for first free color
            for i in range(0, n):
                if not C[i]:
                    break
            CT[v] = i

        # we're findind the number of colors (rounds)
        number_of_colors = max(CT)

        self.prepare_date_list(number_of_colors)

        for v in range (number_of_colors+1):
            print(f"\nRound {v+1} - {self.date_list[v]}:")
            for k in range (n):
                if v != CT[k]:
                    continue
                print(f"{self.vertices[k].vertex}")

    def create_graph_file(self) -> None:
        """ Create file which will be used to draw the graph """
        graph_file = open("graph_file", "w")
        graph_file.write("graph G{\n")

        for i in range(self.number_of_vertices):
            for j in range(self.number_of_vertices):
                if self.edges[i][j].edge == "." or i == j:
                    continue
                graph_file.write(f"\t\"{self.vertices[i].vertex}\" -- \"{self.vertices[j].vertex}\";\n")
                self.remove_edge(self.vertices[j].vertex, self.vertices[i].vertex)
        graph_file.write("}\n")


    def set_first_match_date(self, year: int, month: int, day: int) -> None:
        self.first_match_year = year
        self.first_match_month = month
        self.first_match_day = day

    def prepare_date_list(self, number_of_rounds: int) -> None:
        """ Prepare list of days when matches will be played """
        match_date = date(self.first_match_year, self.first_match_month, self.first_match_day)
        self.date_list.append(match_date)
        for i in range(number_of_rounds):
            match_date += timedelta(days = 7)
            self.date_list.append(match_date)


