from itertools import dropwhile
x = []

for i,n in enumerate(nums1):
	lst = list(dropwhile(lambda x: x <= n, nums2[nums2.index(n)+1:]))
	x.append(lst[0] if len(lst) > 0 else -1)

return x
