import csv
from collections import defaultdict
from queue import PriorityQueue
        
class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]
    
    def read_file(self):
        f = open("DFS.csv",'r')
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.edges = defaultdict(list)
        self.weights = defaultdict(int)
        for row in reader:
            no_child = row[1]
            if no_child == '3':
                self.edges[row[0]].append(row[2])
                self.weights[row[0]+row[2]] = row[3]       #weights = local cost
                self.edges[row[0]].append(row[4])
                self.weights[row[0]+row[4]] = row[5]
                self.edges[row[0]].append(row[6])
                self.weights[row[0]+row[6]] = row[7]
            if no_child == '2':
                self.edges[row[0]].append(row[2])
                self.weights[row[0]+row[2]] = row[3]       #weights = local cost
                self.edges[row[0]].append(row[4])
                self.weights[row[0]+row[4]] = row[5]
               # self.hvalve[row[0]] = row[6]
            if no_child =='1':
                self.edges[row[0]].append(row[2])
                self.weights[row[0]+row[2]] = (row[3])
                #self.hvalve[row[0]] = (row[4])
            #self.edges[row[0]].append(row[1])
            #self.weights[row[0]+row[1]] = row[2]

    def get_cost(self, from_node, to_node):
        return int(self.weights[from_node + to_node])    # its return string. So we must convert it into corresponding integer
    
    
def ucs(graph, start, goal):
    li = []
    visited = set()
    queue = PriorityQueue()
    dictonary = defaultdict(list)
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            #print(node)
            visited.add(node)
            
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    dictonary[(node,cost)].append([i,total_cost])
                    queue.put((total_cost, i))
                    
            if node == goal:
                li.append(goal)
                while goal != start:
                    for key,value in dictonary.items():
                        for i in range(0,len(value)):
                            if value[i] == [goal,cost]:
                                goal = key[0]
                                cost = key[1]
                                li.append(goal)
                            
                for i in reversed(li):
                    print(i)
                return

     
graph = Graph()
graph.read_file()
ucs(graph,'S','G')