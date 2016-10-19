import copy

class Foo(object):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

foo = Foo(1)
print foo
a = ['foo', foo]
print 'a: ',a
# b = a[:]
# c = list(a)
# d = copy.copy(a)
# e = copy.deepcopy(a)

b = a[:]
c = list(a)
d = copy.copy(a)
e = copy.deepcopy(a)

# edit orignal list and instance
a.append('baz')
foo.val = 5

print('original: %r\n slice: %r\n list(): %r\n copy: %r\n deepcopy: %r'
      % (a, b, c, d, e))
