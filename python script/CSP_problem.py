from simpleai.search import CspProblem

variables = ('A', 'B', 'C')

#declearing domain for each of the variable
domains = {
    'A': [1, 2, 3],
    'B': [1, 3],
    'C': [1, 2],
}

# a constraint that expects different variables to have different values
def const_different(variables, values):
    return len(values) == len(set(values))  # remove repeated values and count

# a constraint that expects one variable to be bigger than other
def const_one_bigger_other(variables, values):
    return values[0] > values[1]

# a constraint thet expects two variables to be one odd and the other even,
# no matter which one is which type
def const_one_odd_one_even(variables, values):
    if values[0] % 2 == 0:
        return values[1] % 2 == 1  # first even, expect second to be odd
    else:
        return values[1] % 2 == 0  # first odd, expect second to be even

constraints = [
    (('A', 'B', 'C'), const_different),
    (('A', 'C'), const_one_bigger_other),
    (('A', 'C'), const_one_odd_one_even),
]

my_problem = CspProblem(variables, domains, constraints)

from simpleai.search import backtrack

# my_problem = ... (steps from the previous section)

result = backtrack(my_problem)