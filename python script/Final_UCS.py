# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:32:47 2019

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:35:39 2019

@author: hp
"""
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
        f = open("ucs.csv",'r')
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.edges = defaultdict(list)
        self.weights = defaultdict(int)
        for row in reader:   
            self.edges[row[0]].append(row[1])
            self.weights[row[0]+row[1]] = row[2]

    def get_cost(self, from_node, to_node):
        return int(self.weights[from_node + to_node])    # its return string. So we must convert it into corresponding integer
    
    
def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            print(node)
            visited.add(node)

            if node == goal:
                return
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))
     
graph = Graph()
graph.read_file()
ucs(graph,'0','5')