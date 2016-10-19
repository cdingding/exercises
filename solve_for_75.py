'''
(a + (b - c) * d - e) * f = 75

where a, b, c, d, e, and f are unique integers in the range [1, 6].
'''

# The reason to permute the list of int as str is due to
# the fact that int reduces when adding together.

from itertools import permutations

#soln 1: make the list as a string first, see below
x = ''.join([str(y) for y in range(1,7)]) #can not join integers, only strings
def perms(s):
    if len(s)==1: return s
    result=[]
    for i,v in enumerate(s): # enumerate the string
        result += [v+p for p in perms(s[:i]+s[i+1:])]
        # raw_input('continue')
        # print 'result: ', result
    return result

for perm in perms(x):
    a,b,c,d,e,f = [int(z) for z in perm]
    if (a + (b -c) * d -e) * f == 75:
        print a,b,c,d,e,f

# Or use below
def perms(s):
    if len(s) == 1: return s
    result = []
    for i, v in enumerate(s):  # enumerate the string
        result.extend([v + p for p in perms(s[:i] + s[i + 1:])])
        # raw_input('continue')
        # print 'result: ', result
    return result

for perm in perms(x):
    a, b, c, d, e, f = [int(z) for z in perm]
    if (a + (b - c) * d - e) * f == 75:
        print a, b, c, d, e, f


# soln 2
y = range(1,7)
def perms1(s):
    if len(s)==1: return s
    result=[]
    for i,v in enumerate(s): # enumerate the string
        result += [str(v) + str(p) for p in perms1(s[:i]+s[i+1:])]
        # raw_input('continue')
        # print 'result: ', result
    return result

for perm in perms1(y):
    a,b,c,d,e,f = [int(z) for z in perm]
    if (a + (b -c) * d -e) * f == 75:
        print a,b,c,d,e,f

# soln 3: call and use the itertools.permutations function
for perm in permutations(y):
    a,b,c,d,e,f = perm
    if (a + (b -c) * d -e) * f == 75:
        print a,b,c,d,e,f


#soln 4: permute the list directly
def permutList(l): #the two returns are consistent (list of list)
    if len(l) == 1:
        return [l]  #type: list of list
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])
    return res  # type: list of list

for perm in permutList(y):
    a,b,c,d,e,f = perm
    if (a + (b -c) * d -e) * f == 75:
        print a,b,c,d,e,f


# soln 5: permute the list directly
def permutList1(l):
    if len(l) == 0:
        return [[]]
    res = []
    for e in l:
        temp = l[:]
        temp.remove(e)
        res.extend([[e] + r for r in permutList(temp)])
    return res

for perm in permutList1(y):
    a, b, c, d, e, f = perm
    if (a + (b - c) * d - e) * f == 75:
        print a, b, c, d, e, f

# soln 6
def perms2(x): #did not get it right
    if len(x) == 1: return [x]
    result = []
    for i, v in enumerate(x):
        temp = x[:] #must use this to copy, can not modify x
                    # since it will use later for other iterations
        temp.remove(v)
        # result.extend([[v] + p for p in perms2(x[:i]+x[i+1:])])
        for p in perms2(temp):
            result.extend([[v]+p])
        # raw_input('continue')
    return result
for perm in perms2(y):
    a, b, c, d, e, f = perm
    if (a + (b - c) * d - e) * f == 75:
        print a, b, c, d, e, f

#soln 7
print '---------7------'
def permutList2(l):
    if len(l) == 0:
        return [[]]
    res = []
    for e in l:
        temp = l[:]
        temp.remove(e)
        res.extend([e] + r for r in permutList(temp))
    return res

for perm in permutList2(y):
    a, b, c, d, e, f = perm
    if (a + (b - c) * d - e) * f == 75:
        print a, b, c, d, e, f

# def permss(A,k,n):
#     if k == n:
#         return A[0:n]
#     else:
#         for i in xrange(k,n):
#             A[i],A[k] = A[k],A[i]
#             permss(A,k+1,n)
#             A[i],A[k] = A[k],A[i]
#     return A
# for perm in permss(y, 0 , 6):
#     a, b, c, d, e, f = perm
#     print perm
#     if (a + (b - c) * d - e) * f == 75:
#         print a, b, c, d, e, f
# print permss(y, 0 , 6)

