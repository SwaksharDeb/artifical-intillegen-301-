import simpy
import numpy as np
from collections import defaultdict

travel = defaultdict(float)

def generate_interarrival():
    return np.random.exponential(1./3.0)

def generate_service():
    return np.random.exponential(1./4.0)

def generate_travel():
    return np.random.exponential(1./2.0)

def goto(line) :
    global lineNumber
    lineNumber = line 
    
def cafe_run(env,servers):
    #travel = defaultdict(float)
    i = 0
    while i<=5:
        i += 1
        yield env.timeout(generate_service())
        #travel[i] = generate_travel()
        env.process(truck(env,i,servers))
        
wait_t = []

def truck(env,truck,servers):
    with servers.request() as request:
        t_arrival = env.now
        print(env.now,"truck '%s' arrive "%(truck))
        yield request
        print(env.now,"truck '%s' being served"%(truck))
        yield env.timeout(generate_service())
        print(env.now,"truck '%s' departs "%(truck))
        t_depart = env.now
                    #print(env.now,"truck '%s' arrive "%(truck))
                    #print(env.now,"customer '%s' being served "%(i))
                    #yield env.timeout(generate_service())
                    #travel[i] = generate_travel()
                    #print(env.now,"customer '%s' departs "%(i))        
        if truck <= 6: 
            cafe_run(env,servers)
        wait_t.append(t_arrival - t_depart)
        
env = simpy.Environment()
servers = simpy.Resource(env,capacity = 1)
env.process(cafe_run(env,servers))
env.run(until=10)
        