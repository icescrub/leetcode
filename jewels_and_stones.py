class Solution:
    def numJewelsInStones(self, J, S):
        return(len([1 for j in J for s in S if s == j]))

"""
Alternative solution. This is more direct. Instead of two loops, it just performs one lookup.

class Solution(object):
    def numJewelsInStones(self, J, S):
        lookup = set(J)
        return sum(s in lookup for s in S)
"""
