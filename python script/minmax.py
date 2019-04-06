import csv
from collections import defaultdict

class Minmax:
    def __init__(self):
        self.edges = {}
        self.weights = {}
        
    def read_file(self):
        i = 1
        f = open("minmax.csv",'r')
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.edges = defaultdict(list)
        self.weights = defaultdict(int)
        for row in reader:
            if i == 1:
                self.edges[row[0]].append(row[1])
                self.edges[row[0]].append(row[2])
                i = i + 1
            else:
                self.edges[row[0]].append(row[1])
                self.edges[row[0]].append(row[2])
                self.weights[row[1]] = row[3]
                self.weights[row[2]] = row[4]
    
    def generate_child(self,node):
        return self.edges[node]
    
    def min_max(self,start,depth,maxplaying):
        if depth==0:
            return int(self.weights[start],10)
        if maxplaying:
            maxeval = float("-inf")
            for child in self.generate_child(start):
                eval = self.min_max(child,depth-1,False)
                maxeval = max(maxeval,eval)
            return maxeval
        
        else:
            mineval = float("inf")
            for child in self.generate_child(start):
                eval =self.min_max(child,depth-1,True)
                mineval = min(mineval,eval)
            return mineval
                   

minmax = Minmax()
minmax.read_file()
minmax.min_max('A',2,maxplaying = True)