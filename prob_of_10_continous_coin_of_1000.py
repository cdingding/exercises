# Recurrence relationship

def pf(n):
    if n<10: return 0
    elif n==10: return pow(0.5,10)
    elif n == 11: return pf(10) + pow(0.5, 11)
    return pf(n-1) + (1-pf(n-11))/2.0**11

print pf(13)

