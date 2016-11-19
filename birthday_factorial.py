# stop early factorial
def fact(n,m):
  if n == (365-m+1): #filter the situations by return
    return 365-m+1
  return n*fact(n-1,m)

print 1- float(fact(365,23))/pow(365, 23)

def factorial(n):
  if n == 0:
    return 1
  return n*factorial(n-1)

print factorial(4)