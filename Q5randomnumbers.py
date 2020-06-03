#a) Using a decent built-in uniform deviate generator (or one from an external library – either
#way, justify your choice), write a short program to compute 10^5 uniformly-distributed random
#numbers over the interval x ∈ [0, 1], based on a single seed. Plot the resultant distribution
#as a binned histogram, with the value of x on the x axis and the number of samples in the
#bin on the y axis. Choose an appropriate number of bins.

import time as T

import numpy as np

import matplotlib.pyplot as plt

# to return same results every run use one seed

np.random.seed(1)

s = np.random.uniform(0,1,10**5)

#count, bins, ignored = plt.hist(s,50,density=True)

fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)

axs[0].hist(s, bins=50,density = True)

# plots straight line at y = 1

axs[0].plot([0,1], [1,1], color = 'r')

axs[0].set_title('Uniform distribution')

axs[0].set(ylabel = 'Probability density')

#b) compute random numbers distributed over [0,pi] for 0.5sin(x)

# transformation method

#x is the uniform deviate number

T1 = T.time()

x = np.random.uniform(0,1,10**5)

#y is the calculated PDF which uses x
#integrate from 0 to y
#re-arrange to find inverse for y

y = np.arccos(1-2*x)

#time to generate 10**5 samples for transformation method

T2 = T.time()

axs[1].hist(y, bins=100,density = True)

axs[1].plot(np.linspace(0,np.pi), 0.5*np.sin(np.linspace(0,np.pi)), color = 'r', label = 'True pdf')

axs[1].set_title('Transformation method')

legend = axs[1].legend()

print("time to generate 10**5 samples for transformation method: " + str(T2-T1))

#time to plot here should not be included

T3 = T.time()

#c) compute random numbers over [0,pi]

# rejection method

# comparison function f(y) = C > P(y) everywhere

#  1. pick a random number y_i, uniform y_min to y_max.

#  2. pick p_i random number, uniform 0 to C.

#  3. if P(y_i) < p_i reject y_i and go to step one again using transformation. else accept

#  the accepted y_i will have the desired distribution P(y).

#  efficiency = 1/C *1/y_max - y_min

#  to return same results every run use one seed

np.random.seed(1)

yiaccepted = 0

nosamples = 10**5

# list of the samples accepted

y_i = []

while yiaccepted < nosamples:

    #pick a random number between 0 and 1

    xi = np.random.uniform(0,1)

    # will have the distribution across 0,pi

    yf = np.arccos(1-2*xi)

    xii = yf

    # comparison function

    fy = (2/np.pi) * np.sin(xii)

    ymax = fy

    y = np.random.uniform(0,ymax)

    # pdf

    Py = (2/np.pi) * (np.sin(xii))**2

    if Py > y:

        y_i.append(xii)

        yiaccepted += 1

# time for rejection method to produce 10**5 samples (T4-(T3-T2)-T2)

T4 = T.time()

print("time to generate 10**5 samples for rejection method: " + str(T4-(T3-T2)-T2))

ratio = (T4-(T3-T2)-T2)/(T2-T1)

print(ratio)

# plot y_i s as hisogram

axs[2].hist(y_i, bins=100,density = True)

axs[2].plot(np.linspace(0,np.pi), (2/np.pi) * (np.sin(np.linspace(0,np.pi)))**2, color = 'r', label = 'True pdf')

axs[2].plot(np.linspace(0,np.pi), (2/np.pi)*np.sin(np.linspace(0,np.pi)), color = 'b', label = 'Comparison function')

axs[2].set_title('Rejection method')

legend = axs[2].legend()

plt.show()

    























