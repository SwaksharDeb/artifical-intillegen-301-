from utils import argmin_random_tie, count, first
from collections import defaultdict

class CSP():
    def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem. If variables is empty, it becomes domains.keys()."""
        variables = variables or list(domains.keys())

        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        """Add {var: val} to assignment; Discard the old value if any."""
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """Remove {var: val} from assignment.
        DO NOT call this if you are changing a variable to a new value;
        just call assign for that."""
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        """Return the number of conflicts var=val has with other variables."""
        # Subclasses may implement this more efficiently
        def conflict(var2):
            return (var2 in assignment and
                    not self.constraints(var, val, var2, assignment[var2]))
        return count(conflict(v) for v in self.neighbors[var])

    # These methods are for the tree and graph-search interface:

    def choices(self, var):
        """Return all values for var that aren't currently ruled out."""
        return (self.curr_domains or self.domains)[var]

    def support_pruning(self):
        """Make sure we can prune values from domains. (We want to pay
        for this only if we use it.)"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        """Start accumulating inferences from assuming var=value."""
        self.support_pruning()
        
        """ adding other colors to var state """
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        
        self.curr_domains[var] = [value]
        return removals

    
"""_____________________________________________________________________________________________"""

def first_unassigned_variable(assignment, csp):
    """The default variable order."""
    first = ([var for var in csp.variables if var not in assignment])
    return first[0]

def no_inference(csp, var, value, assignment, removals):
    return True

def unordered_domain_values(var, assignment, csp):
    """The default value order."""
    return csp.choices(var)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """[Figure 6.5]"""

    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment)== 0:
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value) #storing other colors for the state
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                #csp.restore(removals)
        #csp.unassign(var, assignment)
        #return None

    result = backtrack({})                        #passing empty dictonary as assignment
    #assert result is None or csp.goal_test(result)
    return result

"""_________________________________________________________________________________"""

class UniversalDict:
    """A universal dict maps any key to the same value. We use it here
    as the domains dict for CSPs in which all variables have the same domain.
    >>> d = UniversalDict(42)
    >>> d['life']
    42
    """

    def __init__(self, value): self.value = value

    def __getitem__(self, key): return self.value

    def __repr__(self): return '{{Any: {0!r}}}'.format(self.value)


def different_values_constraint(A, a, B, b):
    """A constraint saying two neighboring variables must differ in value."""
    return a != b


def MapColoringCSP(colors, neighbors):
    """Make a CSP for the problem of coloring a map with different colors
    for any two adjacent regions. Arguments are a list of colors, and a
    dict of {region: [neighbor,...]} entries. This dict may also be
    specified as a string of the form defined by parse_neighbors."""
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    csp =  CSP(list(neighbors.keys()), UniversalDict(colors), neighbors,
               different_values_constraint)
    result = backtracking_search(csp)
    print(result)

def parse_neighbors(neighbors, variables=None):
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
        A = A.strip()                        #remove begining and end character from string
        for B in Aneighbors.split():
            dic[A].append(B)
            dic[B].append(A)
    return dic


australia = MapColoringCSP(list('RGB'),
                           'SA: WA NT Q NSW V; NT: WA Q; NSW: Q V; T: ')

