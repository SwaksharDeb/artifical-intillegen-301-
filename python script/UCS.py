# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:35:39 2019

@author: hp
"""

from collections import defaultdict
from queue import PriorityQueue

"""class Graph():
    def __init__(self):
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight"""
        
class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[from_node + to_node]
    
    
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
graph.edges = {'A': ['B', 'C'],
    'B': ['D', 'A'],
    'C': ['A'],
    'D': ['B']
}

graph.weights = {'A'+'B':1,
                 'A'+'C':3,
                 'B'+'D':2,
                 'B'+'A':4,
                 'C'+'A':5,
                 'D'+'B':1
                 }

ucs(graph,'A','D')

