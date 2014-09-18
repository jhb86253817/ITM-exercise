#! /usr/bin/python 

__author__ = "Haibo Jin"

import nltk
from operator import itemgetter

#exercise 2.1 of information theoretic modeling
#a simple inplementation of Huffman coding, based on bigrams

def preprocessing(filename):
    """generate a new file which only contatins lower case alphabet and spaces."""
    file_in = open(filename, 'rb')
    file_out = open(filename+'_preprocess', 'wb')
    text = file_in.read()
    file_in.close()
    text_ = [l.lower() for l in text if l.isalpha() or l==' ']
    for l in text_:
        file_out.write(l)
    file_out.close()
    return text_ 

def mapping(text):
    """use Huffman coding to map all the characters to a binary string"""
    fdist = nltk.FreqDist(text)
    #adjust the format
    tree = [(k[0]+k[1],v) for k,v in fdist.items()]
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
        if isinstance(node[0], list) and len(node[0]) > 1:
            queue.append((node[0][0], node[1]+'0'))
            queue.append((node[0][1], node[1]+'1'))
        else:
            mapping[node[0]] = node[1]
    return mapping

def encoding(text, mapping):
    """encode the given file using the given mapping code."""
    file_out = open('alice_encoded', 'wb')
    text = [l1 + l2 for l1,l2 in text]
    for l in text:
        file_out.write(mapping[l])
    file_out.close()

def decoding(filename, mapping):
    """decode the given file consisting binary strings using the previous mapping."""
    #reverse the dict
    mapping = {v:k for k,v in mapping.items()}

    file_in = open(filename, 'rb')
    file_out = open('alice_recover', 'wb')
    codes = file_in.read()

    current = ''
    for code in codes:
        current += code
        if current in mapping.keys():
            file_out.write(mapping[current])
            current = ''
    file_in.close()
    file_out.close()

def evaluate(filename):
    """output the length of given binary file."""
    file_in = open(filename, 'rb')
    binarys = file_in.read()
    file_in.close()
    return  len(binarys)
        
if __name__ == '__main__':
    text = preprocessing('alice')
    text = zip(text[0::2], text[1::2])
    mapping = mapping(text)
    encoding(text, mapping)
    decoding('alice_encoded', mapping)
    print 'length of encoded binaries:', evaluate('alice_encoded')
