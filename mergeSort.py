def merge(A, B):
    c = []
    i = 0
    j = 0
    n = len(A)
    while i < n and j < n:
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        elif A[i] == B[j]:
            c.append(A[i])
            c.append(B[j])
            i += 1
            j += 1
        else:
            c.append(B[j])
            j += 1
    return c

def findMedian(A, B):
    c = merge(A, B)
    l = len(c)
    idx = l / 2
    if len(c) % 2 == 0:
        md =  (c[idx] + c[idx - 1]) * 0.5
    else:
        md = c[idx]
    return md

A = [1,2,6,4]
B = [3,5,7,3]

print merge(A,B)
print findMedian(A,B)

def quickSort(c):
    if len(c) <= 1:
        return c
    l = len(c)
    pivot = c[-1]
    middle = [x for x in c if x == pivot]
    left = [x for x in c if x < pivot]
    right = [x for x in c if x > pivot]
    return quickSort(left) + middle + quickSort(right)
C = A + B
print quickSort(C)
print sorted(C)
