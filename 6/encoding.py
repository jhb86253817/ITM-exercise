import nltk
data=open('data').read()
from collections import Counter
data=data.split()
data2=nltk.bigrams(data)
data3=nltk.trigrams(data)
c=list(Counter(data3).items())
from operator import itemgetter
c=sorted(c,key=itemgetter(1),reverse=True)
print c
    
