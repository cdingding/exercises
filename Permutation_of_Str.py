# Permutation of Strings
import copy

from itertools import permutations

def perm(A,k,n):
    if k == n:
        print "".join(A[0:n])
    else:
        for i in xrange(k,n):
            A[i],A[k] = A[k],A[i]
            perm(A,k+1,n)
            A[i],A[k] = A[k],A[i]

def permu_string(string):
    for word in permutations(string):
        print word
    perms = [''.join(p) for p in permutations(string)]
    print len(perms)
    return perms

def perms(s):
    if len(s)==1: return s
    result=[]
    for i,v in enumerate(s): # enumerate the string
        result += [v+p for p in perms(s[:i]+s[i+1:])]
        # raw_input('continue')
        # print 'result: ', result
    return result

def product(s):
    d = ((x,y,z) for x in s for y in s for z in s)
    return d.next()

if __name__ == "__main__":
    strS = "Din"
    result1 = []
    # for x in perm(list(strS),0,len(strS)):
    #     result1.append(x)
    # print result1
    # print perm(list(strS), 0, len(strS))
    # print permu_string('Ding')
    print perms('ABC')
    s = '10'
    d = ([x, y, z, w] for x in s for y in s for z in s for w in s)
    print 'd:',d
    rt = []
    for i in range(16):
        rt.append(''.join(d.next()))
    print len(list(set(rt)))
    print list(set(rt))
    # print 'generator as iterator: ---'
    # print [x for x in d.next()] #does not work
    print [''.join([x, y, z, w]) for x in s for y in s for z in s for w in s]
