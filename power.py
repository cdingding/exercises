def power(m,n): #recursion
    if n == 0: return 1
    return m*power(m,n-1)

print power(3,3)