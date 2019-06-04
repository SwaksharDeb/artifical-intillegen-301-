import csv
from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def _init_(self):
        self.edges = {}
        
    def neighbors(self, node):
        return self.edges[node]
    
    def read_file(self):
        f = open("DFS.csv",)
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.edges = defaultdict(list)
        for row in reader:   
            no_child = row[1]
            if no_child == '3':
                self.edges[row[0]].append(row[2])
                self.edges[row[0]].append(row[3])
                self.edges[row[0]].append(row[4])
            if no_child == '2':
                self.edges[row[0]].append(row[2])
                self.edges[row[0]].append(row[3]) 
            if no_child =='1':
                self.edges[row[0]].append(row[2])
            
def bfs(graph, start, goal):
    dictonary = defaultdict(list)
    li = []
    visited = set()
    queue = PriorityQueue()
    queue.put((0,start))
    #queue = deque([start])
    while queue:
        depth, node = queue.get()
        if node not in visited:
            visited.add(node)
            
            child_depth = depth + 1
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    dictonary[(node,depth)].append([neighbor,child_depth])
                    
                    """Using this block of statement for storing our final path to the list named li for
                    backtracking"""
                    if neighbor == goal:
                        li.append(goal)
                        while goal != start:
                            for key,value in dictonary.items():
                                for i in range(0,len(value)):
                                    if value[i] == [goal,child_depth]:
                                        goal = key[0]
                                        child_depth = key[1]
                                        li.append(goal)
                                    
                        """Using this block of statement for backtracking the final path"""
                        for i in reversed(li):
                            print(i)
                        return
                    
                    else:
                        queue.put((depth+1,neighbor))

graph = Graph()
graph.read_file()
bfs(graph,'S','G')
