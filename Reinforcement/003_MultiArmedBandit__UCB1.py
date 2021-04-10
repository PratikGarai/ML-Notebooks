# Uses the concept of confidence for selecting bandits. Bandits that have been used
# higher number of times can be more sure.

# So we user Chernoff Hoedding bound to combine the concept of bound with mean
# and the choice paramenter becomes :
#   Mean + Sqrt(2*log(n)/N)
#       Here , n is the number of times the bandit has been used
#              N is the total number of times played

# The code is same as OIV except for the argmax finding part  => Line 175

import numpy as np
import matplotlib.pyplot as plt
import math

# the old code
class Bandit_1:
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

    bandits = [Bandit_1(m1), Bandit_1(m2), Bandit_1(m3)]

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


class Bandit_2:
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

def oiv_e(m1, m2, m3, N, upper_limit = 10):
    # m1, m2, m3    : 3 different bandits, for each arm
    # N             : the number of times we play
    # no eps anymore
    # upper_limit   : the unreasonably high value

    bandits = [Bandit_2(m1, upper_limit), Bandit_2(m2, upper_limit), Bandit_2(m3, upper_limit)]

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

class Bandit_3:
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

def ucb_e(m1, m2, m3, N, upper_limit = 10):
    # m1, m2, m3    : 3 different bandits, for each arm
    # N             : the number of times we play
    # no eps anymore
    # upper_limit   : the unreasonably high value

    bandits = [Bandit_3(m1, upper_limit), Bandit_3(m2, upper_limit), Bandit_3(m3, upper_limit)]

    # store the results here
    data = np.empty(N)

    # UCB IMPLEMENTATION STARTS HERE
    for i in range(N):

        # same code as OIV, only change in this parameter
        # Adding a 1 to the denominator to make sure division by zero does't occur
        # Adding a 1 to number of trials to make sure log(0) doesn't occur
        j = np.argmax([b.mean+(2*math.log(i+1)/(b.N+1))**0.5 for b in bandits])

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
    oiv = oiv_e(1.0, 2.0, 3.0, 100000)
    ucb = ucb_e(1.0, 2.0, 3.0, 100000)
    
    # log scale plot
    plt.plot(eps, label='eps = 0.1')
    plt.plot(oiv, label='optimistic')
    plt.plot(ucb, label='ucb')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(eps, label='eps = 0.1')
    plt.plot(oiv, label='optimistic')
    plt.plot(ucb, label='ucb')
    plt.legend()
    plt.show()
