from graph import Graph
from data_from_user import DataFromUser
    
if __name__ == "__main__":
    input_data = DataFromUser()
    input_data.start()
    my_graph = Graph()
    my_graph = my_graph.create_graph(input_data.teams_names)
    my_graph.set_first_match_date(input_data.first_match_year, input_data.first_match_month, input_data.first_match_day)
    my_graph.color_the_graph()
    my_graph.create_graph_file()
