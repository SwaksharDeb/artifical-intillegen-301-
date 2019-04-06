from collections import defaultdict

value = ['R','G','B']
variable_domain = {'SA':['R','G','B'], 'WA':['R','G','B'], 'NT':['R','G','B'], 'Q':['R','G','B'],
                'NSW':['R','G','B'], 'V':['R','G','B'], 'T':['R','G','B']
                }

class Grapclouring:
    def __init__(self, variables,domain, variable_domain, neighbour_state):
        self.variables = variables
        self.domains = domain
        self.variable_domain = variable_domain
        self.neighbors = neighbour_state
        self.curr_domains = None
        
    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val
    
    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}
        
    def check_constrain(self, A, a, B, b):                  # B = assignt variable and value
        if a != b:
            return True
        else:
            return False
     
    def prune(self, var, value):
        """Rule out var=value."""
        self.variable_domain[var].remove(value)
 
    def first_unassigned_variable(self, assignment):
        """The default variable order."""
        for var in self.variables:
            if var not in assignment:
                return var
    
    def AC3(self, assignment, queue=None, removals=None,):
        """[Figure 6.3]"""
        if queue is None:
            queue = [(Xi, Xk) for Xi in assignment for Xk in self.neighbors[Xi]]
            #self.support_pruning()
        while queue:
            (Xi, Xj) = queue.pop(0) 
            if self.revise(Xi, Xj, assignment):
                if not self.variable_domain[Xi]:          # if the domain(colour) of parent state is empty
                    return False
                for Xk in self.neighbors[Xj]:          # if any element from domain is deleted then check if the incoming constrain is arc consistence
                    if Xk != Xi:
                        queue.append((Xj, Xk))
        return True


    def revise(self, Xi, Xj, assignment):
        """Return true if we remove a value."""
        revised = False
        for y in self.variable_domain[Xj]:
            if Xi in assignment:
            # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
                if all(not self.check_constrain(Xi, x, Xj, y) for x in assignment[Xi]): #head = neighbour state
                    self.prune(Xj, y)
                    revised = True
            else:
                if all(not self.check_constrain(Xi, x, Xj, y) for x in variable_domain[Xi]): #head = neighbour state
                    self.prune(Xj, y)
                    revised = True

        return revised

    def backtracing(self,assignment):
        if len(assignment) == len(self.variables):
            print(assignment)
            return assignment
        else:
            var = self.first_unassigned_variable(assignment)
            for value in variable_domain[var]:
                """if self.check_constrain(var, value, assignment)== 0:"""
                self.assign(var, value, assignment)
                self.AC3(assignment)    
                self.backtracing(assignment)        
        
def parse_neighbors(neighbors):
    """Convert a string of the form 'X: Y Z; Y: Z' into a dict mapping
    regions to neighbors. The syntax is a region name followed by a ':'
    followed by zero or more region names, followed by ';', repeated for
    each region name. If you say 'X: Y' you don't need 'Y: X'.
    >>> parse_neighbors('X: Y Z; Y: Z') == {'Y': ['X', 'Z'], 'X': ['Y', 'Z'], 'Z': ['X', 'Y']}
    True
    """
    dic = defaultdict(list)
    specs = [spec.split(':') for spec in neighbors.split(';')]     #Split a string into a list where each word is a list item
    for (A, Aneighbors) in specs:
        A = A.strip()
        for B in Aneighbors.split():
            dic[A].append(B)
            dic[B].append(A)
    return dic
    
neighbour_state =  parse_neighbors('SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: ')
australia = Grapclouring(list(neighbour_state.keys()),value, variable_domain, neighbour_state)
australia.backtracing({})
