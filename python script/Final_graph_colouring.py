import csv
from collections import defaultdict

class Graph:
    def __init__(self):
        self.colors = ['Green', 'Blue', 'Red']
        self.states = []
        self.neighbors = {}
        self.colors_of_states = {}

    def read_file(self):
        f = open("graph_colouring.csv",'r')
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.neighbors = defaultdict(list)
        for row in reader:
            no_of_child = row[1]
            if no_of_child == '3':
                self.states.append(row[0])
                self.neighbors[row[0]].append(row[2])
                self.neighbors[row[0]].append(row[3])
                self.neighbors[row[0]].append(row[4])
            if no_of_child == '2':
                self.states.append(row[0])
                self.neighbors[row[0]].append(row[2])
                self.neighbors[row[0]].append(row[3])
                #self.weights[row[1]] = row[3]
                #self.weights[row[2]] = row[4]
            if no_of_child =='4':
                self.states.append(row[0])
                self.neighbors[row[0]].append(row[2])
                self.neighbors[row[0]].append(row[3])
                self.neighbors[row[0]].append(row[4])
                self.neighbors[row[0]].append(row[5])


    def promising(self,state, color):
        for neighbor in self.neighbors[state]: 
            color_of_neighbor = self.colors_of_states.get(neighbor)          ##The get() method is used to avoid such situations. This method returns the value for the given key, if present in the dictionary. If not, then it will return None (if get() is used with only one argument).
            if color_of_neighbor == color:
                return False

        return True

    def get_color_for_state(self,state):
        for color in self.colors:
            if self.promising(state, color):
                return color

    def main(self):
        for state in self.states:
            self.colors_of_states[state] = self.get_color_for_state(state)
        print (self.colors_of_states)

clouring = Graph()
clouring.read_file()
clouring.main()