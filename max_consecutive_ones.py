class Solution:
    def findMaxConsecutiveOnes(self, nums):
        locate_zeros = [-1] + [i for i,x in enumerate(nums) if x == 0] + [len(nums)]
        return max(y-x-1 for x,y in zip(locate_zeros,locate_zeros[1:]))
