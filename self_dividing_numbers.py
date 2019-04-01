# list 1: acceptable numbers.
accepts = [x for x in range(left, right + 1) if str(x).count('0') == 0]

# list 2: modulus of the digits of acceptable numbers.
mod = [[x%int(digit) for digit in str(x)] for x in accepts]

# only choose number for which its mesh = 0.
answer = [num for num,mesh in zip(accepts,mods) if sum(mesh) == 0]

return answer

=============

ALT SOLUTION: More clear. No casting from int to str to int. Just do the math for it.

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isDividingNumber(num):
            n = num
            while n > 0:
                if (n%10) == 0 or (num%(n%10)) != 0:
                    return False
                n /= 10
            return True

        result = []
        for num in xrange(left, right+1):
            if isDividingNumber(num):
                result.append(num)
        return result
