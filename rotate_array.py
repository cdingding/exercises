# 1st way
def rotate(lst, k):
    a_len = len(lst)
    result = lst[-k:]
    result.extend(lst[:a_len-k])
    return result

# 2nd inplace
def rotate_pop(lst, k):
    m = 0
    k %= len(lst)
    while m < k:
        # temp = lst[-1] #space O(1)
        # lst.pop()  #time: O(1)
        lst.insert(0, lst.pop())   #time O(n)
        m += 1
    return lst

# l1 = [0 1 2 3 4 5] --> i = 0, tt= 1, [0 0 2 3 4 5] --> i =1, tt =

# inplace
def rotate1by1(lst, k):
    k %= len(lst)
    m = 0
    while m < k:
        l = len(lst) - 1  #index compantiable
        tt = lst[l]
        while l > 0: # start from the backend, and do minus, better to arrange.
            lst[l] = lst[l-1]
            # print lst
            l -= 1
            # print l
        lst[0] = tt
        m += 1
    return lst


class Solution: #best way to do this
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    lst = range(7)
    print lst
    lst1 = range(7)
    print lst1
    k = 8
    print 'result: \n'
    print rotate_pop(lst,k)
    Solution().rotate(lst1,k)
    print lst1
