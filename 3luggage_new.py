
def luggage_ordering(weights):
    containerWeight = 40
    lug_list = [int(x) for x in weights.split(',')]
    container_list = []
    count = 0
    container = []
    for lug in lug_list:
        count += lug
        if count >= containerWeight:
            container_list.append(container)
            container = []                   # empty container
            count = 0                        # count reset
        container.append(lug)
        print container_list
    container_list.append(container)
    container_list.reverse()
    result = [x for c in container_list for x in c]
    return ' '.join([str(x) for x in result])

def luggage_ordering1(weights): # Put together, sort, and optimize
    limit = 40
    luglist = [int(x) for x in list(weights.split(','))]
    luglist.sort()
    luglist.reverse()
    container_list = []
    container = []
    currentMax = max(luglist)
    myset = set()
    for i,lug1 in enumerate(luglist):
        if lug1==limit:
            container_list.append([lug1])
            continue
        container.append(lug1)
        for j,lug2 in enumerate(luglist[i+1:]):
            containerWeight = sum(container)
            if containerWeight+lug2>limit:
                continue
            if containerWeight+lug2 == limit:
                container.append(lug2)
                luglist.remove(lug2)
                break
            if containerWeight+lug2<limit:
                container.append(lug2)
                luglist.remove(lug2)
        container_list.append(container)
        container = []
    container_list = reduce(lambda x,y:x+y,container_list)
    return container_list

if __name__ == '__main__':
    #print luggage_ordering('2,1,1,1,30,5,6,39,40')
    print luggage_ordering1('2,1,1,1,30,5,6,39,40')

    #Dynamic removing element ahead
    a = [1, 2, 3, 4, 5, 6]
    for i, e in enumerate(a):
        print('e is: ', e)
        for j, f in enumerate(a[i + 1:]):
            if f % 2 == 0:
                a.remove(f)

    ('e is: ', 1)
    ('e is: ', 3)
    ('e is: ', 5)
