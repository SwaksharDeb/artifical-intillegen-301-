GAMMA = 0.9
ALL_POSSIBLE_ACTIONS = {'Cool':['Slow','Fast'], 'Warm':['Slow','Fast'], 'Overheated':['_']}
STATE = ('Cool' , 'Warm', 'Overheated' )
transitions = {('Cool','Slow'):[[1,'Cool',1]],('Cool','Fast'):[[0.5,'Cool',2],[0.5,'Warm',2]],
                ('Warm','Slow'):[[0.5,'Cool',2],[0.5,'Warm',2]],('Warm','Fast'):[[1,'Overheated',-10]]
                ,('Overheated','_'):[[0,'Overheated',0]]
                }
no_of_step = 0
V = {'Cool':0,'Warm':0,'Overheated':0}
  
def value_iteration(epsilon):
  x = globals()['no_of_step']
  delta = 2
  
  while delta > epsilon:
      print("")
      print("_______________________________________________________________________")
      print("")
      V_previous = V.copy()
      #print("ID of V_previous: ",id(V_previous))
      for s in STATE:
          best_a = None
          best_value = float('-inf')
              
          for a in ALL_POSSIBLE_ACTIONS[s]:
              expected_v = 0
              for prob, state_prime, r in transitions[(s,a)]:
                  expected_v += prob * r + GAMMA * prob * V[state_prime]
              if expected_v > best_value:
                  best_value = expected_v
                  V[s] = expected_v
                  best_a = a
          print("for state",s,"best action is: ",best_a)
          print(V)
          for i in STATE:
              delta = max(epsilon, abs(V[s] - V_previous[s]))
              globals()['no_of_step'] += 1
              
value_iteration(0.001)
