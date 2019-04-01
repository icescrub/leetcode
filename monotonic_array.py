class Solution:
    def isMonotonic(self, A):

        def negative(lst):
            return all(x <= 0 for x in lst)
        def positive(lst):
            return all(x >= 0 for x in lst)
        
        diff = [y-x for x,y in zip(A,A[1:])]
        return positive(diff) or negative(diff)
