
def quick_sort(lst):
    if len(lst) <= 1: return lst
    pivot = lst[len(lst)/2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

print quick_sort([12,6,3,8,10,1,34,2,12,23,2,5,34,32,1])