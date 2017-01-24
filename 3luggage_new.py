
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

if __name__ == '__main__':
    print luggage_ordering('2,1,1,1,30,5,6,39,40')