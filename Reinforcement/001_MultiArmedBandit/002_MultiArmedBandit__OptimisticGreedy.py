# In this case, we do not use epsilon at all, but we go straight for a greed
# However, during initalization, our estimated mean is kept unreasonably high, 
# so that the graph can't help but only go down, eventually going towrds the
# real value

# Advantage : Unexplored machines get explored eventually

# the old code
class Bandit_Old:
    def __init__(self, m):
        # m       : true mean
        # mean    : our estimate of bandits mean
        # N       : number of attempts (sample size) 
        self.m = m
        self.mean = 0
        self.N = 0

    def pull(self):
        # randn returns stuff with unit variance and mean 0
        # empty randn() returns a single float that is then 
        # added to the true mean
        return np.random.randn() + self.m
    
    def update(self, x):
        # new mean = (old mean * (N-1) + new value)/N
        self.N += 1
        self.mean = (1.0*self.mean*(self.N-1) + x)/self.N

def eps_e(m1, m2, m3, eps, N):
    # m1, m2, m3    : 3 different bandits, for each arm
    # eps           : epsilon, the threshold probability
    # N             : the number of times we play

    bandits = [Bandit_Old(m1), Bandit_Old(m2), Bandit_Old(m3)]

    # store the results here
    data = np.empty(N)


    # EPSILON GREEDY IMPLEMENTATION STARTS HERE
    for i in range(N):
        p = np.random.random()      # the random number
        if p<eps :
            # try a random machine
            j = np.random.choice(3)
        else :
            # choose the best machine
            j = np.argmax([b.mean for b in bandits])
        
        # pull the machine and update it's mean
        x = bandits[j].pull()
        bandits[j].update(x)

        # for plotting purpose 
        data[i] = x

    cumulative_average = np.cumsum(data)/(np.arange(N)+1)

    plt.plot(cumulative_average)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    # logarithmic scale
    plt.xscale('log')
    plt.show()

    for b in bandits :
        print(b.mean)

    return cumulative_average

import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, m, upper_limit):
        # m             : true mean
        # upper_limit   : the unreasonable assumption
        # N             : number of attempts (sample size) 
        self.m = m
        self.mean = upper_limit
        self.N = 0

    def pull(self):
        # randn returns stuff with unit variance and mean 0
        # empty randn() returns a single float that is then 
        # added to the true mean
        return np.random.randn() + self.m
    
    def update(self, x):
        # new mean = (old mean * (N-1) + new value)/N
        self.N += 1
        self.mean = (1.0*self.mean*(self.N-1) + x)/self.N

def run_experiment(m1, m2, m3, N, upper_limit = 10):
    # m1, m2, m3    : 3 different bandits, for each arm
    # N             : the number of times we play
    # no eps anymore
    # upper_limit   : the unreasonably high value

    bandits = [Bandit(m1, upper_limit), Bandit(m2, upper_limit), Bandit(m3, upper_limit)]

    # store the results here
    data = np.empty(N)


    # OPTIMISTIC GREEDY IMPLEMENTATION STARTS HERE
    for i in range(N):

        # direct greedy implementation
        j = np.argmax([b.mean for b in bandits])

        # pull the machine and update it's mean
        x = bandits[j].pull()
        bandits[j].update(x)

        # for plotting purpose 
        data[i] = x

    cumulative_average = np.cumsum(data)/(np.arange(N)+1)

    plt.plot(cumulative_average)
    plt.plot(np.ones(N)*m1)
    plt.plot(np.ones(N)*m2)
    plt.plot(np.ones(N)*m3)
    # logarithmic scale
    plt.xscale('log')
    plt.show()

    for b in bandits :
        print(b.mean)

    return cumulative_average

if __name__=='__main__':
    eps = eps_e(1.0, 2.0, 3.0, 0.1, 100000) 
    oiv = run_experiment(1.0, 2.0, 3.0, 100000)
    
    # log scale plot
    plt.plot(eps, label='eps = 0.1')
    plt.plot(oiv, label='optimistic')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(eps, label='eps = 0.1')
    plt.plot(oiv, label='optimistic')
    plt.legend()
    plt.show()
