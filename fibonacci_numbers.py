
def fibo_gen(lst, start, end):
    # lst with two above numbers
    # fibo sequence: 1, 1, 2, 3, 5, 8 ...
    if start == 1 and len(lst) == 1: yield 1
    else: yield sum(lst[-2:])

def fibo_gen1(limit):
    # fibo sequence: 1, 1, 2, 3, 5, 8 ...
    result = [1,1]
    if limit < 1: yield 0
    if limit == 1: yield result[0]
    while result[-1] <= limit:
        result.append(sum(result[-2:]))
        # result.pop(0)
    yield result[:-1]


def f(n): #fibonacci generator
    if n < 0: return 0
    if n == 1 or n == 0: return 1
    result = []
    result.append(f(n - 1) + f(n - 2))
    return f(n-1) + f(n-2)


def fact(n): #factorial generator
    if n < 0 : return 'n must be positive!'
    if n == 0: return 1
    return n*fact(n-1)

if __name__ == '__main__':
    print f(10)
    print [f(i) for i in range(11)]
    print map(f,range(11))
    print fact(5)
    for x in fibo_gen1(100):
        print x


