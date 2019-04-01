# My original solution. Super slow.

    def twoSum(self, nums, target):
        nums2 = [2*x - target for x in nums]
        answer = ([i,j] for i,x in enumerate(nums2) for j,y in enumerate(nums2) if x == -y and i != j)
        return next(answer)

"""
Alternative solution is much faster.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
"""
