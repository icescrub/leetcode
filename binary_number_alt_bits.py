Step 1: Strip the binary number, create list of its binary digits.
Step 2: Zip up each digit with its neighbor bit. Compare their sum to 1 (only 1 + 0 == 1, thus alternating bits == 1).
Step 3: If all neighboring bits have sum == 1, then number has all alternating bits.

class Solution:
    def hasAlternatingits(self, n):
        lst = [int(x) for x in bin(n)[2:]]
        c = [x+y == 1 for x,y in zip(lst,lst[1:])]
        return all(c)
