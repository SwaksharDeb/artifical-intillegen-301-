from simpleai.search import CspProblem

variables = ('WA', 'NT', 'Q','NSW','V','SA','T')

#declearing domain for each of the variables
domains = {
    'WA': ['RED', 'GREEN', 'BLUE'],
    'NT': ['RED', 'GREEN', 'BLUE'],
    'Q': ['RED', 'GREEN', 'BLUE'],
    'NSW':['RED', 'GREEN', 'BLUE'],
    'V':['RED', 'GREEN', 'BLUE'],
    'SA':['RED', 'GREEN', 'BLUE'],
    'T':['RED', 'GREEN', 'BLUE']
    }
    
adjacency = {'WA' :['NT','SA'],
             'NT' : ['SA','Q'],
             'SA' : ['NT','Q','NSW','V'],
             'NSW' : ['SA','V','Q'],
             'V':['NSW','SA'],
             'T':[]
}

i = 0

"""for row in adjacency:
    length = len(adjacency[row])
    for i in range(length):
        if domains([row]) not in domains[adjacency[row][i]]:
            None
            
            """

def const_different(variables, values):
    return len(values) == len(set(values)) 

constraints = [
    (('WA','NT'), const_different),
    (('WA','SA'),const_different),
    (('NT','Q'),const_different),
    (('SA','NT'),const_different),
    (('SA','Q'),const_different),
    (('SA','NSW'),const_different),
    (('SA','V'),const_different),
    (('NSW','V'),const_different),
    (('NSW','Q'),const_different),
]

my_problem = CspProblem(variables, domains, constraints)

from simpleai.search import backtrack

# my_problem = ... (steps from the previous section)

result = backtrack(my_problem)