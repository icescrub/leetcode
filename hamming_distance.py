# Hamming Distance is the number of bits that are different between two numbers.

class Solution:
    def hammingDistance(self, x, y):

	# This is the bitwise XOR operation. This gives us the number whose binary representation is the XOR of the other two numbers.
	z = x ^ y
	
	# Take the binary representation, strip the '0b' part of the string, and return the number of 1's.

        return bin(z).strip('0b').count('1')
