import csv
from collections import defaultdict

class Pruning:
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
    
    def Alpha_Beta(self,position,alpha,beta,depth,maxplaying):
        if depth==0:
            return int(self.weights[position])
        if maxplaying == True:
            maxeval = float("-inf")
            #alpha = float("-inf")
            #beta = float("inf")
            for child in self.generate_child(position):
                eval =self.Alpha_Beta(child,alpha,beta,depth-1,False)
                maxeval = max(maxeval,eval)
                alpha = max(alpha,eval)
                if alpha >= beta:
                    break
            return maxeval
        else:
            mineval = float("inf")
            #alpha = float("-inf")
            #beta = float("inf")
            for child in self.generate_child(position):
                eval = self.Alpha_Beta(child,alpha,beta,depth-1,True)
                mineval = min(mineval,eval)
                beta = min(beta,eval)
                if alpha >= beta:
                    break
            return mineval
        
alpha_beta = Pruning()
alpha_beta.read_file()
alpha_beta.Alpha_Beta(position = 'A',alpha = float("-inf"),beta = float("inf"),depth = 2,maxplaying = True)