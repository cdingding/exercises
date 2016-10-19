
def product_n2(lst):
    result = []
    # Iter and calculate product
    for index, item in enumerate(lst):
        i = 0
        product_before_index = 1
        product_after_index = 1
        print index
        while i < index:
            product_before_index = product_before_index*lst[i]
            i += 1
        m = index+1
        while m <= (len(lst)-1):
            product_after_index = product_after_index*lst[m]
            m += 1
        result.append(product_before_index*product_after_index)
    return result

def product_n(lst):
    result = []
    # Iter and calculate product
    result = [None]*len(lst)
    i = 0
    product_before_index = 1
    product_after_index = 1
    while i < index:
        product_before_index = product_before_index[i]*lst[i]
        i += 1
    m = index+1
    while m <= (len(lst)-1):
        product_after_index = product_after_index*lst[m]
        m += 1
    result.append(product_before_index*product_after_index)
    return result

if __name__=="__main__":
    lst = [0, 7, 3, 4]
    print product_n2(lst)
    print product_n(lst)