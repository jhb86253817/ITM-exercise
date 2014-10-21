from __future__ import division
from math import gamma, log, factorial

__author__ = "Haibo Jin"

"""
Exercise 1 and 2 of week 5, compute the code-length of Markov Chain model with zero-order, first-order and second-order.
"""

def beta(a,b):
    return gamma(a)*gamma(b)/gamma(a+b)

def split_chain(data, order):
    if order==0:
        return data 
    elif order==1:
        data1=''
        data2=''
        for i in range(1,len(data)):
            if data[i-1] == '0': data1 += data[i]
            else: data2 += data[i]
        return data1, data2
    else:
        data1=''
        data2=''
        data3=''
        data4=''
        for i in range(2,len(data)):
            if data[i-2]=='0' and data[i-1]=='0': data1 += data[i] 
            elif data[i-2]=='0' and data[i-1]=='1': data2 += data[i]
            elif data[i-2]=='1' and data[i-1]=='0': data3 += data[i]
            else: data4 += data[i]
        return data1, data2, data3, data4

def zero_order_prob(data, a, b):
    """compute the probability of the given data under zero-order model using mixture code."""
    count_zero = data.count('0')
    count_one = data.count('1')
    return beta(count_one+a, count_zero+b)/beta(a, b)

def choose(n, k):
    """compute the value of n choose k."""
    return factorial(n)/factorial(k)/factorial(n-k)


def zero_order_prob2(data):
    """compute the probability of the given data under zero-order model using NML code."""
    c = 0
    n = len(data)
    for k in range(n+1):
        c += choose(n, k) * (k/n)**k * ((n-k)/n)**(n-k)
    count_zero = data.count('0')
    count_one = data.count('1')
    prob_ml = (count_one/n)**count_one * (count_zero/n)**count_zero
    return prob_ml/c

    

if __name__ == '__main__':
    #the given data
    data = "1111001001111011111101110011111111111111110110111010111111111000101011111001111111011110101101111110"

    print '---------------------------------------------------------------------------------------'
    print 'This is mixture model (exercise 1):\n'

    #zero order
    prob = zero_order_prob(data, 0.5, 0.5)
    print 'probability of the data under zero-order model:', prob 
    print 'code-length of the data under zero-order model:', -log(prob, 2)
    
    #first order
    data1, data2 = split_chain(data, 1)
    prob = 0.5 * zero_order_prob(data1, 0.5, 0.5) * zero_order_prob(data2, 0.5, 0.5)
    print 'probability of the data under first-order model:', prob 
    print 'code-length of the data under first-order model:', -log(prob, 2)

    #second order
    data1, data2, data3, data4 = split_chain(data, 2)
    prob =  0.25 * zero_order_prob(data1, 0.5, 0.5) * zero_order_prob(data2, 0.5, 0.5) * zero_order_prob(data3, 0.5, 0.5) * zero_order_prob(data4, 0.5, 0.5)
    print 'probability of the data under second-order model:', prob 
    print 'code-length of the data under second-order model:', -log(prob, 2)

    print '---------------------------------------------------------------------------------------'
    print 'This is NML model (exercise 2):\n'

    #zero order
    prob = zero_order_prob2(data)
    print 'probability of the data under zero-order model:', prob 
    print 'code-length of the data under zero-order model:', -log(prob, 2)
    
    #first order
    data1, data2 = split_chain(data, 1)
    prob = 0.5 * zero_order_prob2(data1) * zero_order_prob2(data2)
    print 'probability of the data under first-order model:', prob 
    print 'code-length of the data under first-order model:', -log(prob, 2)

    #second order
    data1, data2, data3, data4 = split_chain(data, 2)
    prob =  0.25 * zero_order_prob2(data1) * zero_order_prob2(data2) * zero_order_prob2(data3) * zero_order_prob2(data4)
    print 'probability of the data under second-order model:', prob 
    print 'code-length of the data under second-order model:', -log(prob, 2)



