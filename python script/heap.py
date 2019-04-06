# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:01:44 2019

@author: hp
"""

from collections import defaultdict
from queue import PriorityQueue

class Heap:
    def _init_(self):
        self.edges = []
        #self.node = []
        
    def Input(self):
        for i in range(5):
            a = int(input("enter a number: "))
            self.edges.append(a)
            
    def heap(self):
        queue = PriorityQueue()
        cost = 0
        for edge in self.edges:
            for a in self.edges:
                if edge>a:
                    cost = cost+1
            #self.node.append((cost,edge))
            queue.put(cost,edge)
            cost = 0
        for i in range(5):
            a , node = queue.get()
            print(node)
            
heap = Heap()
heap.Input()
heap.heap()