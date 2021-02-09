from datetime import date

class DataFromUser:
    def __init__(self):
        self.first_match_year = ""
        self.first_match_month = ""
        self.first_match_day = ""
        self.number_of_teams = 0
        self.teams_names = []

    def start(self):
        """ The main function that will ask user all necessary questions """
        self.ask_user_for_number_of_teams()
        self.ask_user_for_names()
        self.ask_user_first_match_data()

    def ask_user_for_names(self) -> None:
        self.ask_user_for_number_of_teams()
        print("Enter teams names: ")

        for i in range (self.number_of_teams):
            self.teams_names.append(input(f"{i+1}. "))

    def ask_user_for_number_of_teams(self) -> None:
        while not isinstance(self.number_of_teams, int) or self.number_of_teams < 2:
            self.number_of_teams = input("Enter number of teams: ")
            try:
                self.number_of_teams = int(self.number_of_teams)
                if self.number_of_teams < 2:
                    print("\nNumber of teams need to be a positive integer (larger than one!)\nPlease try again.\n")
            except:
                print("\nNumber of teams need to be a positive integer (larger than one!)\nPlease try again.\n")

    def ask_user_first_match_data(self) -> None:
        is_correct = False
        input_data = ""
        while not is_correct:
            try:
                input_data = input("Enter the date of the first match: (format - YYYY/MM/DD): \n")
                input_data = input_data.split("/")
                self.first_match_year = int(input_data[0])
                self.first_match_month = int(input_data[1])
                self.first_match_day = int(input_data[2])
                date(self.first_match_year, self.first_match_month, self.first_match_day)
                is_correct = True
            except:
                print("\nIncorrect date. Try again.\n")


