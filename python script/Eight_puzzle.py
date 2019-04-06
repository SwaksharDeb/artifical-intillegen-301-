from collections import defaultdict

closed = []
edges =  defaultdict(list)

class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = tuple(data)
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'_')
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
                edges[self.data].append(child)
        edges[self.data] = tuple(edges[self.data])
        return children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data) and puz not in closed:
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            temp_puz = [tuple(l) for l in temp_puz]
            temp_puz = tuple(temp_puz)
            return temp_puz
        else:
            return None
    
    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            #t = tuple(t)
            temp.append(t)
        temp = tuple(temp)
        return temp    
            
    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j
    def backtrack(self,start,goal,Path):
        if start.data in edges[goal]:
            #Path.append(start.data)
            return start.data
            
        else:
            for i in edges:
                if goal in edges[i]:
                    Path.append(i)
                    return self.backtrack(start,i,Path)
            #key = list(edges.keys())[tuple(edges.values()).index(goal)]
            #print(key)

class Puzzle(Node):
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")          #The split() method splits a string into a list.You can specify the separator, default separator is any whitespace.
            temp = tuple(temp)
            puz.append(temp)
        puz = tuple(puz)
        return puz

    def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        function_value = start.level+((self.h(start.data,goal)+self.mhd(start.data,goal))/2)
        return function_value

    def h(self,start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
    
    def mhd(self,start,goal):
        manhatan_distance = 0
        for x in range(1,9):
            for i in range(0,self.n):
                for j in range(0,self.n):
                    if start[i][j] == '_':
                        continue
                    elif x == int(start[i][j]):
                        x1 = i
                        y1 = j
                        break
                    else:
                        continue
                    break
            for i in range(0,self.n):
                for j in range(0,self.n):
                    if goal[i][j] == '_':
                        continue
                    elif x == int(goal[i][j]):
                        x2,y2 = i,j
                        break
                    else:
                        continue
                    break
            manhatan_distance += abs(x1-x2) + abs(y1-y2)
            
            #x1,y1 = start.find(start.data,x)
            #x2,y2 = start.find(goal,x)
        return manhatan_distance
        
    def process(self):
        """ Accept Start and Goal Puzzle state"""
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")        
        goal = self.accept()

        start = Node(start,0,0)
        start.fval = self.f(start,goal)
        self.open.append(start)
        print("\n\n")
        f1 = open('8_Puzzle.txt','w')
        print("Doing A* search to find goal: ")
        f1.write("Doing A* search to find goal: \n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            f1.write(str(cur.data))
            f1.write("\n")
            print("local cost of above state is: ",cur.level)
            print("hreustic value of above state is: ",((self.h(cur.data,goal)+self.mhd(cur.data,goal))/2))
            print("functional value of above state is: ",self.f(cur,goal))
            hreustic = ((self.h(cur.data,goal) + self.mhd(cur.data,goal))/2)
            function_value = self.f(cur,goal)
            local_cost = cur.level
            
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data,goal) == 0):
                print("Final path is: ")
                f1.write("Final path is: \n")
                Path = [goal]
                Path.append(self.backtrack(start,goal,Path))
                Final_Path = (reversed(Path))
                a = len(Path) -1
                for i in Final_Path:
                    print(i)
                    f1.write(str(i))
                    f1.write("\n")
                print("total step is: ",a)
                f1.write("total step is: ")
                f1.write(str(a))
                f1.write("\n")
                f1.write("Local cost is: ")
                f1.write(str(local_cost))
                f1.write("\n")
                f1.write("Final hreustic is: ")
                f1.write(str(hreustic))
                f1.write("\n")
                f1.write("Final functional value is: ")
                f1.write(str(function_value))
                f1.write("\n")
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal)
                self.open.append(i)
            closed.append(cur.data)
            del self.open[0]
            """ sort the opne list based on f value """
            self.open.sort(key = lambda x:x.fval,reverse=False)

puz = Puzzle(3)
puz.process()

