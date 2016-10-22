
def luggage1(weights):
    containerWeight = 40
    lug_list = [int(x) for x in weights.split(',')]
    container_list = []
    count = 0
    container = []
    for i, lug in enumerate(lug_list):
        count += lug
        # lug_list.remove(lug)
        if count < containerWeight:
            container.append(lug)
        if count >= containerWeight:
            container_list.append(container)
            count = 0
            container = []
            container.append(lug)
            # print container_list,container
        if i == len(lug_list)-1 and container not in container_list:
            container_list.append(container)
    container_list.reverse()
    result = [x for container in container_list for x in container]
    return ','.join([str(x) for x in result])

print luggage1('2,1,1,1,30,5,6,39')