lst1 = []
def foo(lst):
    lst.append(1)
    return lst
print foo(lst1)
print foo(lst1)
print foo(lst1)

def foo1(i=[]):
    i.append(1)
    return i

print foo1()
print foo1()

def foo2():
    i = []
    i.append(1)
    return i
print foo2()
print foo2()