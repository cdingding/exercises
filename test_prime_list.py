from math import sqrt

def is_prime(n):
  if n <= 1:
    return False
  for i in xrange(2, int(sqrt(n) + 1)):
    if n % i == 0:
      return False
  return True

def prime_generator():
    n = 900
    while n <= 1000:
        if is_prime(n):
            yield(n)
        n = n + 1
        
if __name__ == '__main__':
    result = []
    for val in prime_generator():
        result.append(val)
    print result
