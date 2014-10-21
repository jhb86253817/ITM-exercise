from __future__ import division
from math import factorial, log 
from subprocess import call, check_output

__author__ = "Haibo Jin"

"""
exercise 2.1, week 6 of information theoretic modeling
"""

def choose(n, k):
    """compute the value of n choose k."""
    return factorial(n) / (factorial(k) * factorial(n-k))

def bernoulli_c(n):
    """calculate c with sample size=n, under bernoulli model."""
    c = 0
    for k in range(n+1):
        c += choose(n, k) * (k/n)**k * ((n-k)/n)**(n-k)
    return c

def multi_c(n, m):
    """calculate c with sample size=n, under m-ary multinomial model."""
    if m == 1:
        return 1
    elif m == 2:
        return bernoulli_c(n)
    else:
        return multi_c(n, m-1) + n/(m-2) * multi_c(n, m-2)

def prob_nml(counts):
    """calculate the nml probability given the counts of different ary."""
    n = sum(counts)
    m = len(counts)
    p_ml =1 
    for c in counts:
        p_ml *= (c/n)**c
    return p_ml / multi_c(n, m)

def fnml(structure):
    """given the structure of bayesian network, compute code-length of every factor using fNML."""
    groups =  check_output(["python", "splitcfg.py", "survey.txt", structure[0], structure[1], structure[2], structure[3], structure[4], structure[5]])
    groups = groups.split('\n')
    groups = [map(int, ll.split()) for ll in groups if len(ll)>0]
    lengths = [-log(prob_nml(ll), 2) for ll in groups]
    print "The total conde-length:",  sum(lengths)
    

if __name__ == '__main__':
    fnml(["1 2", " ", " ", " ", " ", " "])
    
