#! /usr/bin/python 

__author__ = "Haibo Jin"

"""
exercise 2 of week 3 from Information Theoretic Modeling.
"""

from operator import itemgetter
from math import log, ceil

codewords = {}

def sf_encode(probs):
    """use Shannon-Fano coding to encode the given symbols with probabilities."""
    #sort the probabilities in decreasing order
    probs = sorted(probs.items(), key = itemgetter(1), reverse = True)
    #initialize all codewords as empty string
    for key,value in probs:
        codewords[key] = ''
    split(probs)

def split(probs):
    """split the two sets with probabilities as much as equal, and recursively do the same for subsets."""
    if len(probs) == 1:
        return
    prob_sum = sum(v for k,v in probs)
    diff_min = 1.0
    index_min = -1
    for i in range(1,len(probs)):
        first_sum = sum(v for k,v in probs[:i])
        second_sum = prob_sum - first_sum
        if abs(first_sum - second_sum) < diff_min:
            diff_min = abs(first_sum - second_sum)
            index_min = i
    #adding 0 or 1 for two sets 
    for i in range(index_min):
        codewords[probs[i][0]] += '0'
    for i in range(index_min, len(probs)):
        codewords[probs[i][0]] += '1'
    #recursively call split() for two subsets
    split(probs[:index_min])
    split(probs[index_min:])

def expect_length(probs):
    """return the expected code-length of given symbols."""
    expect = 0.0
    for k,v in probs.items():
        expect += v * len(codewords[k])
    return expect
        
def entropy(probs):
    """return the entropy of given probabilities."""
    return sum(-v*log(v,2) for v in probs.values())

def expect_sh_length(probs):
    """return the expected code-length of shannon code."""
    return sum(v*ceil(-log(v,2)) for v in probs.values())

if __name__ == '__main__':
    probs = {'A':0.9, 'B':0.02, 'C':0.04, 'D':0.01, 'E':0.015, 'F':0.015}
    sf_encode(probs)
    print codewords
    print "expected code-length:", expect_length(probs)
    print "entropy:", entropy(probs)
    print "expected code-length of shannon code:", expect_sh_length(probs)

