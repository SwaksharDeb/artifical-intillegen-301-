import csv
from collections import defaultdict

class Expectiminmax:
    def __init__(self):
        self.edges = {}
        self.weights = {}
        
    def read_file(self):
        f = open("alpha_beta.csv",'r')
        reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
        self.edges = defaultdict(list)
        self.weights = defaultdict()
        for row in reader:
            no_of_child = row[1]
            if no_of_child == '3':
                self.edges[row[0]].append(row[2])
                self.edges[row[0]].append(row[3])
                self.edges[row[0]].append(row[4])
            if no_of_child == '2':
                self.edges[row[0]].append(row[2])
                self.edges[row[0]].append(row[3])
                #self.weights[row[1]] = row[3]
                #self.weights[row[2]] = row[4]
            if no_of_child =='0':
                self.weights[row[0]] = row[2]
    
    def generate_child(self,node):
        return self.edges[node]
    
    def Min_Max(self,position,depth,maxplaying,minplaying):
        if depth==0:
            return int(self.weights[position])
        if maxplaying == True:
            maxeval = float("-inf")
            #alpha = float("-inf")
            #beta = float("inf")
            for child in self.generate_child(position):
                eval =self.Min_Max(child,depth-1,False,True)
                maxeval = max(maxeval,eval)
                return maxeval
        
        elif minplaying == True:  
            mineval = float("inf")
            #alpha = float("-inf")
            #beta = float("inf")
            for child in self.generate_child(position):
                eval = self.Min_Max(child,depth-1,False,False)
                mineval = min(mineval,eval)
                return mineval
                
        else:
            expect = 0
            for child in self.generate_child(position):
                v = self.Min_Max(child,depth-1,True,False)
                expect  += (1/2)* v
                return expect

        
expectiminmax = Expectiminmax()
expectiminmax.read_file()
expectiminmax.Min_Max(position = 'A',depth = 2,maxplaying = True,minplaying = False)