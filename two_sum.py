from collections import defaultdict

class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for i, item1 in enumerate(nums):
    #         for j, item2 in enumerate(nums[i+1:]):
    #             if (item1 + item2) == target:
    #                 return [i, i+j+1]

    def twoSum1(self, nums, target):
        d = {}
        for i, ie in enumerate(nums):
            d[ie] = i
            for j, je in enumerate(nums):
                if (target - ie) == je and i != j:
                    return [i, j]

    def twoSum2(self, num, target):
        d = {}
        for i, e in enumerate(num):
            if e in d:
                return [d[e], i]
            d[target - e] = i

    def twoSum3(self, num, target):
        d = defaultdict(list)
        result = []
        for i, e in enumerate(num):
            if e in d:
                d[e].append(i)
            d[target - e].append(i)
        return [value for key, value in d.iteritems() if len(value) > 1][0]

    def twoSum4(self, num, target):
        d = defaultdict(list)
        for i, e in enumerate(num):
            d[e].append(i)
            if target - e in d and target - e != e:
                d[target - e].append(i)
        return [value for key, value in d.iteritems() if len(value) > 1][0]

num = [3,2,4]
target = 6
print Solution().twoSum1(num, target)
print Solution().twoSum2(num, target)
print Solution().twoSum3(num, target)
print Solution().twoSum4(num, target)


