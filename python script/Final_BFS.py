# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:49:23 2019

@author: hp
"""

import csv
from collections import defaultdict
from collections import deque

class Graph:
    def _init_(self):
        self.edges = {}
        
    def neighbors(self, node):
        return self.edges[node]
    
    def read_file(self):
        f = open("bfs.csv",)
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.edges = defaultdict(list)
        for row in reader:   
            self.edges[row[0]].append(row[1])

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    print(start)
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    print(neighbor)
                    if neighbor == goal:
                        return
                    queue.appendleft(neighbor)

graph = Graph()
graph.read_file()
bfs(graph,'A','D')