sA, sB = sum(A), sum(B)
delta = (sB - sA)//2
for a in set(A):
	if a+delta in set(B):
		return [a,a+delta]
return []
