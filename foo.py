lst1 = []
def foo(lst):
    lst.append(1)
    return lst
print foo(lst1)
print foo(lst1)
print foo(lst1)
print '--------'
def foo1(i=[]):
    i.append(1)
    return i

print foo1()
print foo1()
print '------'
def foo2():
    i = []
    i.append(1)
    return i
print foo2()
print foo2()
print '-----'
i = []
def foo3():
    i.append(1)
    return i
print foo3()
print foo3()