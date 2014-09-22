#! /usr/bin/python 

__author__ = "Haibo Jin"

"""
exercise 3 of week 3 from Information Theoretic Modeling.
"""

from operator import itemgetter
from math import log, ceil 
from shannon_fano import *  
from nltk import FreqDist

def get_probs(filename):
    """read the given text and calculate the probabilities for all symbols."""
    with open(filename) as file_in:
        text = file_in.read()
    probs = FreqDist(text)
    count_sum = sum(v for v in probs.values())
    for k,v in probs.items():
        probs[k] = v * 1.0 / count_sum
    return probs

if __name__ == '__main__':
    probs = get_probs('alice_preprocess')
    sf_encode(probs)
    print codewords
    print "expected code-length:", expect_length(probs)
    print "entropy:", entropy(probs)
    print "expected code-length of shannon code:", expect_sh_length(probs)
