class Solution:
    def addDigits(self, num):
        m = num
        
        while m > 9:
            m  = sum([int(x) for x in list(str(m))])
            
        return m
