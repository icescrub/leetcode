# Why? 2x all UNIQUE numbers in the list would give, minus all numbers in the set gives me the missing doubled number.

class Solution:
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)
