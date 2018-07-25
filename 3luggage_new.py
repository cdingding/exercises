
def luggage_ordering(weights): # Real time, no optimization, BigO(n)
    containerWeight = 40
    lug_list = [int(x) for x in weights.split(',')]
    lug_list.sort()
    lug_list.reverse()
    container_list = []
    count = 0
    container = []
    for lug in lug_list:
        if count+lug <= containerWeight:
            container.append(lug)
            count += lug
            continue
        container_list.append(container)
        container = [lug]                   # empty container
        count = lug             # count reset
    if count>0:
        container_list.append(container)
    print('container list: ',container_list)
    # container_list.reverse()
    result = [x for c in container_list for x in c] # c must be before x, otherwise c is not defined
    return ' '.join([str(x) for x in result])

# Add 3 luggage limit also
def luggage_ordering3(weights): # Real time, no optimization, BigO(n)
    containerWeight = 40
    lug_list = [int(x) for x in weights.split(',')]
    lug_list.sort()
    lug_list.reverse()
    container_list = []
    count = 0
    container = []
    for lug in lug_list:
        if (count+lug <= containerWeight)&(len(container)<3):
            container.append(lug)
            count += lug
            continue
        container_list.append(container)
        container = [lug]                   # empty container
        count = lug            # count reset
    if count>0:
        container_list.append(container)
    print('container list: ',container_list)
    # container_list.reverse()
    result = [x for c in container_list for x in c] # c must be before x, otherwise c is not defined
    return ' '.join([str(x) for x in result])



def luggage_ordering1(weights, limit = 40): # Put together, sort, and optimize # not sort reverse need 4 containers
    # BigO(n^2)
    luglist = [int(x) for x in list(weights.split(','))]
    # luglist.sort()
    # luglist.reverse()
    container_list = []
    container = []
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
            container.append(lug2)
            luglist.remove(lug2)
        container_list.append(container)
        container = []
    # container_list = reduce(lambda x,y:x+y,container_list)
    return container_list

def luggage_ordering2(weights, limit = 40): # Put together, sort, and optimize # with sort reverse need 3 containers
    luglist = [int(x) for x in list(weights.split(','))]
    luglist.sort()
    luglist.reverse()
    container_list = []
    container = []
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
            container.append(lug2)
            luglist.remove(lug2)
        container_list.append(container)
        container = []
    # container_list = reduce(lambda x,y:x+y,container_list)
    return container_list



if __name__ == '__main__':
    #print luggage_ordering('2,1,1,1,30,5,6,39,40')
    print luggage_ordering('2,1,1,1,30,6,39,40')

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
