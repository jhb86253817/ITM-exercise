#!/usr/bin/python
#
# splitcfg.py    Teemu Roos  2014
#
# read data array from file and print, for each variable, counts of each value
# broken down by parent configuration.
#
# example:
# > python splitcfg.py survey.txt "1 2" "3" "" "2" "1 2" "2 4"
# 115 57 90
# 63 11 43
# 47 34 22
# 11 2 5
# 366 117
# 13 4
# 365 135
# 358 7
# 125 10
# 96 166
# 63 54
# 34 69
# 8 10
# 79 21 30
# 137 36 62
# 40 19 12
# 34 9 21
#
# where cmd line arguments give the data file name and then the list
# of parents for each variable.
#
# note: cycles are not detected so it's your responsibility to avoid them.

import sys
from math import exp, log
from scipy.misc import comb

if len(sys.argv) < 3:
    print "usage:\n\t" + sys.argv[0] + " <data-file> <par-1> ... <par-K>\n" + \
        "\twhere <par-i> is a list of parant node indices, e.g., \"0 2\""
    sys.exit(9)

fname = sys.argv[1]

# read file
with open(fname) as f:
    header = [varname.strip('"') for varname in f.readline().split()]
    D = f.readlines()

# split file contents into an array
D = [list([s.strip('"\n') for s in row.split(' ')]) for row in D]

p = len(D[0])   # number of variables
n = len(D)      # sample size

# number of values for each variable
vals = [len(set([D[row][i] for row in range(n)])) for i in range(p)]

# parent list from command line arguments
G = [[int(par) for par in s.split(" ") if par != ''] for s in sys.argv[2:]]
if len(G) < p:
    print "not enough parents given (" + str(len(G)) + " < " + str(p) + ")"
    sys.exit(9)

# iterate through variables
for i in range(p):

    # family = parents + node
    fa = G[i] + [i]

    # select data columns corresponding to family
    localData = [tuple([row[var] for var in fa]) for row in D]

    # sort first by parent configuration and then by node value
    localData = sorted(localData)

    # store and print node value counts per parent configuration
    kk = []; k = 0; prev = localData[0]

    for item in localData:
        if item != prev:
            # new child value, store count and create new counter
            kk.append(k)
            k = 0

        if item[:-1] != prev[:-1]:
            # new parent cfg: print and reset counters
            kk = kk + [0] * (vals[i]-len(kk)) # fill in zeros for unobserved x

            # for more detailed output, uncomment the next two lines
            #print "var " + header[i] + " vals: " + str(vals[i]) + \
            #    " cfg: " + str(prev[:-1]) + " kk: " + str(kk)

            print " ".join([str(k) for k in kk])
            kk = []; k = 0

        k += 1
        prev = item

    # last parent cfg: print counters
    kk.append(k)
    kk = kk + [0] * (vals[i]-len(kk)) # fill in zeros for unobserved

    # for more detailed output, uncomment the next two lines
    #print "var " + header[i] + " vals: " + str(vals[i]) + \
    #    " cfg: " + str(prev[:-1]) + " kk: " + str(kk)
    print " ".join([str(k) for k in kk])
