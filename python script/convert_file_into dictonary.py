import csv
from collections import defaultdict

f = open("ucs.csv",'r')
reader =csv.reader(f)                  #store file into 2D list. So reader is a 2D list
edges = defaultdict(list)
weights = defaultdict(int)

for row in reader:   
    edges[row[0]].append(row[1])
    weights[row[0]+row[1]] = row[2]