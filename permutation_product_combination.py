from itertools import permutations

'''
Input: 00?1100?
Output: 00011000, 00111000, 00011001, 00111001

write a function to output all possible 1,0 strings
by replacing ? in the input pattern string to 0, and 1.
'''

aStr = '00?1100?'
str_list1 = aStr.split('?')
str_list2 = aStr.split('?')
print str_list1

switch = ['1','0']
result = []
i = 0
n = len(str_list1)

# Permute same string only
def permu_string(string):
    # for word in permutations(string, r=True):
    #     print word
    perms = [''.join(p) for p in permutations(string,r=3)]
    print len(perms)
    return perms

s = 'AB'
permuted = permu_string(s)
print 'permuted:',permuted

#
# result = []
# while i < (2*(n -1)):
#     a = str_list1.insert(i+1,permuted[0])
#     i += 2
# print len(result)
# print list(set(result))
# print '--------'

# choose 1 from 2 for 4, permute with replacement
import itertools
result = []
def perm(seq, n):
    for p in itertools.product(seq, repeat=n):
        result.append("".join(p))
    return result
ls = perm("AB", 3)
print 'real: ', len(ls), ls

# choose 2 from 3, combinations, no replacement
print list(itertools.combinations('ABCD', 3))

# Choose 3 from 4 and permute, no replacement
aa = ["".join(elem) for elem in itertools.permutations('ABCD',3)]
print len(aa)
print aa
