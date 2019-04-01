import itertools

rows = len(nums)
columns = len(nums[0])
r_n = rows*columns//r

# Flattens list, then cuts it up again into disjoint slices for the new matrix.

if rows*columns == r*c:
	nums_flattened = list(itertools.chain.from_iterable(nums))
	answer = [nums_flattened[r_n*i:r_n*(i+1)] for i in range(r)]
	return answer
else:
	return nums
