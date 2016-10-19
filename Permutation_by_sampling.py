import numpy as np
import random
import math
import matplotlib.pyplot as plt

##1. To get the permutations by sampling
result = set()
result2 = set()
for i in range(100):
    ls = list('din')
    all2 = random.sample(ls,3)
#     all3 = np.random.choice(ls, 4, replace = False)
    result.update([''.join(all2)])
    result2.update([''.join(np.random.choice(ls, 3, replace = False))])
print len(result), list(result)[:5]
print len(result2), list(result2)[:5]

##2. To get the permutations by sampling
result = []
result2 = []
for i in range(1000):
    ls = list('PEPPER')
    all2 = random.sample(ls,6)
#     all3 = np.random.choice(ls, 4, replace = False)
    result += [''.join(all2)]
    result2 += [''.join(np.random.choice(ls, 6, replace = False))]
print len(result),len(set(result)), list(result)[:5]
print len(result2),len(set(result2)), list(result2)[:5]
math.factorial(6)

##3. To get the permutations by sampling
result = []
result2 = []
for i in range(1000):
    ls = list('10')
    all2 = random.sample(ls,2)
#     all3 = np.random.choice(ls, 4, replace = False)
    result += [''.join(all2)]
    result2 += [''.join(np.random.choice(ls, 4, replace = True))] #can change sample len and replace
print len(result),len(set(result)), list(result)[:5]
print len(result2),len(set(result2)), list(result2)[:5]
math.factorial(6)
#
# aa = np.random.randint(0,100,90)
# print aa

##4. Try large set
nn = range(10000)
ss = set()
for i in range(1000):
    ss.update(set(np.random.choice(nn,100)))
print len(ss)
