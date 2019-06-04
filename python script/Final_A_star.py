import csv
from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}
        self.hvalve = {}

    def neighbors(self, node):
        return self.edges[node]
    
    def read_file(self):
        #i = 1
        f = open("A_star.csv",'r')
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.edges = defaultdict(list)
        self.weights = defaultdict(int)
        self.hvalve = defaultdict(int)
        for row in reader:
            no_child = row[1]
            if no_child == '3':
                self.edges[row[0]].append(row[2])
                self.weights[row[0]+row[2]] = row[3]       #weights = local cost
                self.edges[row[0]].append(row[4])
                self.weights[row[0]+row[4]] = row[5]
                self.edges[row[0]].append(row[6])
                self.weights[row[0]+row[6]] = row[7]
                self.hvalve[row[0]] = row[8]
            if no_child == '2':
                self.edges[row[0]].append(row[2])
                self.weights[row[0]+row[2]] = row[3]       #weights = local cost
                self.edges[row[0]].append(row[4])
                self.weights[row[0]+row[4]] = row[5]
                self.hvalve[row[0]] = row[6]
            if no_child =='1':
                self.edges[row[0]].append(row[2])
                self.weights[row[0]+row[2]] = (row[3])
                self.hvalve[row[0]] = (row[4])
            if no_child == '0':
                self.hvalve[row[0]] = (row[2])
        
    def get_cost(self, from_node, to_node):
        c = int(self.weights[from_node + to_node])
        return c        # its return string. So we must convert it into corresponding integer
    
def A_star(graph, start, goal):
    li = []
    visited = set()
    dictonary = defaultdict(list)
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        cost_prime = cost
        if node not in visited:
            #print(node," = ", cost_prime)
            visited.add(node)

            if node == goal:
                li.append(goal)
                while goal != start:
                    for key,value in dictonary.items():
                        for i in range(0,len(value)):
                            if value[i] == [goal,cost_prime]:
                                goal = key[0]
                                cost_prime = key[1]
                                li.append(goal)
                            
                for i in reversed(li):
                    print(i)
                return
            
            for i in graph.neighbors(node):
                if i not in visited:
                    cost = cost - int(graph.hvalve[node])
                    if cost < 0:
                        cost = 0
                    total_cost = cost + int(graph.hvalve[i]) + graph.get_cost(node, i)
                    dictonary[(node,cost_prime)].append([i,total_cost])
                    queue.put((total_cost, i))
                    
            
    
graph = Graph()
graph.read_file()
A_star(graph,'S','G')
