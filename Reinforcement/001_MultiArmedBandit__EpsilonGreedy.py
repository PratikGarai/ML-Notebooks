# Here, we use a threshold value(epsilon). Then, we use random() to get a number
# If the number is less than epsilon, we check-out a new machine. Else, we continue
# using the best machine. Epsilon is usually low (0.05 or 0.1 , i.e., 5% or 10%)

import numpy as np
import matplotlib.pyplot as plt

class Bandit:
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

def run_experiment(m1, m2, m3, eps, N):
    # m1, m2, m3    : 3 different bandits, for each arm
    # eps           : epsilon, the threshold probability
    # N             : the number of times we play

    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

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

if __name__=='__main__':
    c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 100000) 
    c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 100000) 
    c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 100000) 

    # logarithmic plots
    plt.plot(c_1, label='cps=0.1')
    plt.plot(c_05, label='cps=0.05')
    plt.plot(c_01, label='cps=0.01')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plots
    plt.plot(c_1, label='cps=0.1')
    plt.plot(c_05, label='cps=0.05')
    plt.plot(c_01, label='cps=0.01')
    plt.legend()
    plt.show()
