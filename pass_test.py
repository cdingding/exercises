def print1(x):
     if x<0:
         pass
     elif x >0:
         pass
     else:
         print 'ding'

# print1(0)
print1(0)

total, x = 0, 1
while x <= 8:
    if x == 5:
        x += 1
        break
    total += x
    x += 1
    print total, x
print total
print '---above is break result \n'

total, x = 0, 1
while x <= 8:
    if x == 5:
        x += 1
        continue
    total += x
    x += 1
    print total, x
print total
print '---above is continue result \n'

total, x = 0, 1
while x <= 8:
    if x == 5:
        x += 1
        pass
    total += x
    x += 1
    print total, x
print total
print '---above is pass result \n'
