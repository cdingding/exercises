def check(num): # give wrong answer:
    # for example: num =15, i = 2, then else will return True
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in xrange(2,num):
        if num % i == 0:
            return False
        else:
            return True

def check1(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in xrange(2,num):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = 3
    print 'Try %d times: ' % n
    i = 1
    while i < 4:
        n = int(input('Enter a number: '))
        print check1(n)
        raw_input('Hit enter to continue')
        i += 1
