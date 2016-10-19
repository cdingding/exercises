from copy import copy, deepcopy
import numpy as np

class Foo(object):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)
foo = Foo(1)
print foo
a = [np.arange(6), foo, foo]
print a
a = np.array(a)
aa = a
b = a.copy()
bb = copy(a)
c = deepcopy(a)
print 'b: ', b

a[1] =1000
foo.val = 5
# a.append('baz')
a[0][1] =100

print '--------- after change'
print 'a:', a
print 'aa:', aa
print 'b:', b
print 'bb:', bb
print 'c:', c

