# stop early factorial
def fact(n):
  if n == (365-22):
    return 365-22
  return n*fact(n-1)

print float(fact(365))/pow(365, 23)
