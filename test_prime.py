from math import sqrt

def is_prime(n):
  if n < 1:
    return False
  for i in xrange(2, int(sqrt(n) + 1)):
    if n % i == 0:
      return False
  return True

def prime_generator():
    n = 1
    while True:
        if is_prime(n):
            yield(n)
        n = n + 1
        
if __name__ == '__main__':
    lst = [12,23,3,5,31,34,45,67]
    result = []
    for val in lst:
        if is_prime(val):
            result.append(val)
    print result
    result2 = [x for x in lst if is_prime(x) == True]
    print 'By list comprehension: ', result2