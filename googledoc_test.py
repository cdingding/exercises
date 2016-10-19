

n = 15
def check(num):
  print 'ding'
  for i in xrange(2,num):
    print i
  if num % i == 0:
    return 'Not prime!'
  else:
    return 'yes, prime'
    print (check(n))

