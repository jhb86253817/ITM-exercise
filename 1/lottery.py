#! /usr/bin/python 

__author__ = "Haibo Jin"

from scipy.stats import binom
import matplotlib.pyplot as plt 
from math import factorial

#exercise 1.4 of information theoretic modeling
#a binary lottery problem about binomial distribution 

def choose(m, n):
    """return the value of m choose n."""
    return factorial(m) / factorial(n) / factorial(m-n)

def pmf_binom(n, prob, per):
    """given the parameter of binomial distribution, calculate the least number of sum of pmf that can reach the percentage."""
    #generate pmf for all n
    pmf = [(binom.pmf(i, n, prob), i) for i in range(0, n+1)]
    #sort the pmf so that larger pmf is in priority
    pmf = sorted(pmf, reverse=True)
    #draw a plot for visulization
    cdf = []
    sum_pmf = 0.0
    for p,i in pmf:
        sum_pmf += p
        cdf.append(sum_pmf)
    plt.plot(cdf)
    plt.title("cdf of sorted binomial distribution")
    plt.show()

    #calculate the sum of n maximum pmf that satisfy the percentage  
    num = 0
    for c in cdf:
        num += 1
        if c >= per:
            break

    pmf = pmf[:num]
    index = [i for p,i in pmf]
    #buy tickts that has these number of 1
    print "buy these tickets that 1 shows x times:", index
    tickets = 0
    for i in index:
        tickets += choose(n, i)
    print "at least buy this many tickets:", tickets


if __name__ == '__main__':
    pmf_binom(100, 0.1, 0.93)

