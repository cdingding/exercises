import random
import numpy as np

def sampling(lst, k): # Periodic: every k
    return lst[::k]

def mod_sampling(lst, k): # Periodic: every k
    return [lst[i] for i in range(len(lst)) if i % k ==0 ]

def sys_sampling2(lst, k): #random without replacement
    return random.sample(lst, k) #return list

def np_sampling_replace(ls,k): #random with replacement
    return list(np.random.choice(ls, k)) #return list(array)

def np_sampling_no_replace(ls,k): #random without replacement
    return list(np.random.choice(ls, k, replace = False)) #return list(array)

if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print sampling(mylist, 3)
    print mod_sampling(mylist,3)
    print sys_sampling2(mylist, 3)
    print np_sampling_replace(mylist, 3)
    print np_sampling_no_replace('ABCD', 3)