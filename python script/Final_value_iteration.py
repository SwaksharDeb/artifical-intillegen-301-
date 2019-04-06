GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = {'Cool':['Slow','Fast'], 'Warm':['Slow','Fast'], 'Overheated':['_']}
STATE = ('Cool' , 'Warm', 'Overheated' )
transitions = {('Cool','Slow'):[[1,'Cool',1]],('Cool','Fast'):[[0.5,'Cool',2],[0.5,'Warm',2]],
                ('Warm','Slow'):[[0.5,'Cool',2],[0.5,'Warm',2]],('Warm','Fast'):[[1,'Overheated',-10]]
                ,('Overheated','_'):[[0,'Overheated',0]]
                }

def value_iteration(epsilon):

    U = {s: 0 for s in STATE}
    #R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U_1 = U.copy()
        delta = 0
        for s in STATE:
            U[s] = max(sum(p*r + GAMMA*p*U_1[s1] for (p, s1, r) in transitions[(s, a)])  #sum must return something
                                                                                         #so we created two for loop inside sum command
                                                 for a in ALL_POSSIBLE_ACTIONS[s])
            delta = max(delta, abs(U[s] - U_1[s]))
        #print(U)
        if delta <= epsilon*(1 - GAMMA)/GAMMA:
            return U

print(value_iteration(epsilon = 0.001))