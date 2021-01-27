from graph import Graph

def start():
    teams = ask_user_for_names()
    my_graph = Graph()
    my_graph = my_graph.create_graph(teams)
    my_graph.color_the_graph()
    my_graph.create_graph_file()

def ask_user_for_names() -> list:
    teams_names = []
    number_of_teams = ""
    while not isinstance(number_of_teams, int):
        number_of_teams = input("Enter number of teams: ")
        try:
            number_of_teams = int(number_of_teams)
        except:
            print("Number of teams need to be a positive integer\nPlease try again.\n")

    print("Enter teams names: ")

    for i in range (number_of_teams):
        teams_names.append(input(f"{i+1}. "))

    return teams_names

if __name__ == "__main__":
    start()