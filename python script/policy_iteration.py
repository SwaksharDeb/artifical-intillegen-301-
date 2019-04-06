from utils import argmax

GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = {'Cool':['Slow','Fast'], 'Warm':['Slow','Fast'], 'Overheated':['_']}
STATE = ('Cool' , 'Warm', 'Overheated' )
transitions = {('Cool','Slow'):[[1,'Cool',1]],('Cool','Fast'):[[0.5,'Cool',2],[0.5,'Warm',2]],
                ('Warm','Slow'):[[0.5,'Cool',2],[0.5,'Warm',2]],('Warm','Fast'):[[1,'Overheated',-10]]
                ,('Overheated','_'):[[0,'Overheated',0]]
                }
#V = {'1':0, '2':0,'3':0}
#print("ID of V: ",id(V))

def policy_extraction():
   
    U = {s: 0 for s in STATE}
    pi = {'Cool':'Slow','Warm':'Slow','Overheated': '_'}
    while True:
        U = policy_evaluation(pi, U)
        unchanged = True
        for s in STATE:
            a = argmax(ALL_POSSIBLE_ACTIONS[s], key=lambda a: expected_utility(a, s, U))
            if a != pi[s]:
                pi[s] = a
                unchanged = False
        if unchanged:
            return pi


def expected_utility(a, s, U):

    return sum(p*r+GAMMA*p*U[s1] for (p, s1, r) in transitions[(s, a)])


def policy_evaluation(pi, U, k=20):

    for i in range(k):
        for s in STATE:
            if s == 'Overheated':
                U[s] = 0
            else:
                U[s] = sum(p*r + GAMMA*p*U[s1]  for (p, s1, r) in transitions[(s, pi[s])])
    return U

print(policy_extraction())