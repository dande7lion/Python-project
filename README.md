# Python-project

The main functionality of this program is the division of several teams (e.g. in sport league) into rounds, while maintaining the following rules:
* Every team must play against every other team
* No team can play two times in one round (conflict)
Moreover, this program will also 
* print the dates of the rounds 
* create and open graph which was used for division teams

### Technologies
* Python 3.8.5
* Dot (create graph)
* Eog (show graph)

### Setup
To run this program, download these files:
* ```data_from_user.py```
* ```graph.py```
* ```main.py```
* ```run```

and put them into one folder. Then use a command:
```ssh
$ ./run
```

### How to use this program:
* After running program, you'll be asked for give number of teams. Be careful - it must be an integer (greater than 1). Otherwise, the program will inform you about mistake and ask you to give the number again.
* When you give the correct number of teams, program will ask you to enter their names.
* After that, you will be asked for give the date of the first match. Again, you must be careful and give the correct date, otherwise you'll be informed about mistake and asked to try again. 
* When you put all needed information, you'll be shown the graph, which was created by program, and the result - divided teams with match dates.

### Implementation
Program includes two main files: 
* ```data_from_user.py```
* ```graph.py```
and one file that calls specified functions:
* ```main.py```

#### Graph class
Object of this class is a graph. It has vertices and edges between them. Both vertices and edges can have name and value.
In this class we've got some obvious functions, like add_vertex, add_edge etc.
In function create_graph we prepare graph with given information and with these rules:
* vertex  = one match (e.g. 'A - B' (where A and B - teams)
* we add edge between two matches when they **can not** be played in the same round. It means that if we've got vertex 'A - B', we have to connect it with all vertices where is team 'A' or 'B'.
The main functionality is closed in color_the_graph function - greedy algorithm that will color our graph.
Then there is a function that prepares graph_file, which is needed to create graph using Dot program.
Prepare_date_list function prepares the dates of matches. The main thing here is that the matches are played each week at the same day of the week.


#### Data from user class
This is an auxiliary class, that asks user for data (number and names of teams, date of the first match) and checks if it's correct.

### Additional information
* Program creates one files needed to draw graph: ```graph_file```. 
