import itertools
import copy

'''
Input: 00?1100?
Output: 00011000, 00111000, 00011001, 00111001

write a function to output all possible 1,0 strings
by replacing ? in the input pattern string to 0, and 1.
'''

def perm(seq, n):
    result = []
    for p in itertools.product(seq, repeat=n):
        result.append(p)
    return result

if __name__ == '__main__':
    aStr = '00?11?00?'
    str_list = list(aStr)
    indexes = []
    q_num = len([x for x in aStr if x == '?'])
    perms = perm('10', q_num)

    # Soln version 1: copy the original string list, and modify inplace
    results = []
    # for idx, ele in enumerate(str_list):
    #     if ele == '?':
    #         indexes.append(idx)
    indexes = [x for x,y in enumerate(aStr) if y == '?']
    print [x for x, y in enumerate(str_list) if y == '?' ]
    for m, perm in enumerate(perms):
        # temp = copy.copy(str_list)  # must use copy, or all elements in results will change at the same together
        # temp = str_list[:] # or use above or below
        temp = list(str_list) # or use above
        for i in range(q_num):
            temp[indexes[i]] = perm[i]   # index of indexes for temp
        results.append(temp)

    print len(list(set([''.join(x) for x in results])))
    print list(set([''.join(x) for x in results]))


    # Soln version 2: Common index, start from empty string, can avoid copy action, easier to analyze
    m = 0
    result1 = []
    for perm in perms:
        tofill = ''
        k = 0
        for i in range(len(aStr)):
            if str_list[i] != '?':
                tofill = tofill + str_list[i]
            else:
                tofill = tofill + perm[k]
                k += 1
        result1.append(tofill)
    print len(result1)
    print list(set(result1))




