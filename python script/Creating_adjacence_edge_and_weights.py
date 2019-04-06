# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:55:28 2019

@author: hp
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        """self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)               # return list inside a dictonary.Like edges = {'A':['B','C'],'D':['A']}   
        self.weights = {}                            #create a empty dictonary
    
    # create adjacence node and give weight to every corresponding edges
    # Note: assumes edges are bi-directional
    def add_edge(self, from_node, to_node, weight):
        
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight