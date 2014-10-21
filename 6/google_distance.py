from __future__ import division
from math import log
import matplotlib.pyplot as plt


__author__ = "Haibo Jin"

"""
exercise 4, week 6 of information theoretic modeling
"""

def get_pagenum():
    """store the page numbers of each single word and their pairs in a dictionary."""
    page_num = {}
    page_num['Andrey'] = 3180000
    page_num['Kolmogorov'] = 188000
    page_num['complexity'] = 6410000
    page_num['stochastic'] = 6330000
    page_num['porridge'] = 708000
    page_num['Rissanen'] = 325000
    page_num['breakfast'] = 55400000
    page_num['omelette'] = 949000
    page_num['broccoli'] = 3040000
    page_num['Andrey Kolmogorov'] = 64400
    page_num['Andrey complexity'] = 244000000
    page_num['Andrey stochastic'] = 6510000
    page_num['Andrey porridge'] = 345000
    page_num['Andrey Rissanen'] = 1750000
    page_num['Andrey breakfast'] = 393000000
    page_num['Andrey omelette'] = 892000
    page_num['Andrey broccoli'] = 4790000
    page_num['Kolmogorov complexity'] = 487000
    page_num['Kolmogorov stochastic'] = 493000
    page_num['Kolmogorov porridge'] = 14300
    page_num['Kolmogorov Rissanen'] = 367000
    page_num['Kolmogorov breakfast'] = 216000
    page_num['Kolmogorov omelette'] = 6170
    page_num['Kolmogorov broccoli'] = 61000
    page_num['complexity stochastic'] = 6120000
    page_num['complexity porridge'] = 2080000
    page_num['complexity Rissanen'] = 776000
    page_num['complexity breakfast'] = 31000000
    page_num['complexity omelette'] = 2310000
    page_num['complexity broccoli'] = 8370000
    page_num['stochastic porridge'] = 264000
    page_num['stochastic Rissanen'] = 1510000
    page_num['stochastic breakfast'] = 2840000
    page_num['stochastic omelette'] = 113000
    page_num['stochastic broccoli'] = 1200000
    page_num['porridge Rissanen'] = 11000
    page_num['porridge breakfast'] = 6640000
    page_num['porridge omelette'] = 6870000
    page_num['porridge broccoli'] = 618000
    page_num['Rissanen breakfast'] = 201000
    page_num['Rissanen omelette'] = 3670
    page_num['Rissanen broccoli'] = 164000
    page_num['breakfast omelette'] = 11800000
    page_num['breakfast broccoli'] = 13000000
    page_num['omelette broccoli'] = 1040000

    return page_num

def ngd(w1, w2):
    """calculate the normalized google distance between the given two words."""
    page_num = get_pagenum()
    M = 5e10
    distance = (max(log(page_num[w1],2),log(page_num[w2],2)) - log(page_num[w1+' '+w2])) / (log(M,2) - min(log(page_num[w1],2),log(page_num[w2],2)))        
    return distance

def draw(words):
    heatmap = []
    for i in range(0,9):
        temp = []
        for j in range(0,9):
            if i==j: 
                temp.append(0.0)
                continue
            elif i > j:
                temp.append(ngd(words[j], words[i]))
                continue
            temp.append(ngd(words[i], words[j]))
        heatmap.append(temp)

    plt.clf()
    plt.imshow(heatmap)
    plt.show()

if __name__ == '__main__':
    words = ['Andrey', 'Kolmogorov', 'complexity', 'stochastic', 'porridge', 'Rissanen', 'breakfast', 'omelette', 'broccoli']
    for i in range(0,8):
        for j in range(i+1,9):
           print words[i] + ',' + words[j] + ':', ngd(words[i], words[j])
    draw(words)

