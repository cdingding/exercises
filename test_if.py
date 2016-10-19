
num = input('Enter a number:')

def testit(num):
    for i in xrange(2, num):
        if num % i == 0:
            print 'before return'
            return 'Not prime!'
    return 'Yes, prime!'

print testit(num)
