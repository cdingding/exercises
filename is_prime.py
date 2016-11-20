from math import sqrt
'''
A prime number (or a prime) is a natural number
greater than 1 that has no positive divisors other than 1 and itself.
'''

def is_prime(n):
    if n <= 1:
        return False
    for factor in xrange(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True

def prime_generator():
    n = 100
    while n<200:
        if is_prime(n):
            yield(n)
        n += 1

def isPrime(n):
    if n < 2: return False
    for item in xrange(2,int(sqrt(n))+1):
        if n % item == 0:
            return False
    return True

print len([x for x in range(10, 100) if is_prime(x)])
print len([x for x in range(100, 1000) if is_prime(x)])
print len([x for x in range(1000, 10000) if is_prime(x)])
print len([x for x in range(10000, 100000) if isPrime(x)])

if __name__ == '__main__':
    x = []
    for value in prime_generator():
        x.append(value)
    print x
    y = []
    lst = [12,23,25,56,77,67,86,567]
    for item in lst:
        if is_prime(item):
            y.append(item)
    print y