"""
How to find complement?

Suppose num = 5.

bin(5) = 0b101.

Need to mask that with 0b111 and XOR to find its complement.

0b111 XOR 0b101 = 0b010 = 2. Correct answer.

=======

So get bit length of 5.

5.bit_length = 3

1 << 3 = 0b1000 = 8

8 - 1 = 0b111, just what we want as a mask.

Subtract the two numbers.

(8-1) - 5 = 2.

Answer!
"""

def findComplement(self, num):
	return (1 << num.bit_length()) - 1 - num
