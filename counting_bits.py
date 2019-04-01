from itertools import *

def counting_bits(n):
	return sum( (n>>i)&1 for i in range(n.bit_length()) )

========

REAL METHOD:

Step 1: Create building blocks.

def bit_length_me(num):
	count = 0
	while num:
		num >>= 1
		count += 1
	return count

building_blocks = [1<<i for i in range(bit_length_me(num))]

# For 17, building_blocks = [1,2,4,8,16]

Step 2: Map all numbers from 0 to 17 with their building block representation.

valid_numbers = chain.from_iterable(combinations(building_blocks,i) for i in range(1,bit_length_me(num)+1))

filtered = filter(lambda x: sum(x) <= num, valid_numbers)

d = {sum(g):g for g in filtered}

return [0] + [len(d[n]) for n in range(1,num+1)]
