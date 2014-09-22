#! /usr/bin/python 

__author__ = "Haibo Jin"

import nltk
from operator import itemgetter

#supplement of exercise 3 of week 3 from information theoretic modeling
#a simple inplementation of Huffman coding, the source is 'Alice'

def get_probs(filename):
    """read the given text and calculate the probabilities for all symbols."""
    with open(filename) as file_in:
        text = file_in.read()
    probs = nltk.FreqDist(text)
    count_sum = sum(v for v in probs.values())
    for k,v in probs.items():
        probs[k] = v * 1.0 / count_sum
    return probs

def mapping(probs):
    """use Huffman coding to map all the characters to a binary string"""
    tree = probs.items()
    tree = sorted(tree, key = itemgetter(1))
    while len(tree) > 1:
        node = ([tree[0][0], tree[1][0]], tree[0][1]+tree[1][1])
        tree = tree[2:]
        tree.append(node)
        tree = sorted(tree, key = itemgetter(1))

    #for storing the mapping
    mapping = {}
    #for traversing the tree 
    queue = []
    #two children nodes of the root
    left = (tree[0][0][0],'0')
    right = (tree[0][0][1],'1')
    queue.append(left)
    queue.append(right)
    #traversing the tree, encoding the leaves
    while len(queue) > 0:
        node = queue.pop(0)
        if len(node[0]) > 1:
            queue.append((node[0][0], node[1]+'0'))
            queue.append((node[0][1], node[1]+'1'))
        else:
            mapping[node[0]] = node[1]
    return mapping

def expect_length(probs, mapping):
    """return the expected code-length of given symbols."""
    expect = 0.0
    for k,v in probs.items():
        expect += v * len(mapping[k])
    return expect

if __name__ == '__main__':
    probs = get_probs('alice_preprocess')
    mapping = mapping(probs)
    print mapping
    print "expected code-length:", expect_length(probs, mapping)

    #encoding(text, mapping)
    #decoding('alice_encoded', mapping)
    #print 'length of encoded binaries:', evaluate('alice_encoded')
