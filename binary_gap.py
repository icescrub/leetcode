Step 1. Take binary form of N and list it as 1's and 0's.

list_N = list(bin(N).strip('0b'))

Step 2: Create list of indices where bit is 1.

e = [i for i,x in enumerate(list_N) if x == '1']

Step 3: Get difference in pairwise values.

f = [y-x for x,y in zip(e,e[1:])]

NOTE: The method below is slower than the method above, but an optional way of doing things.

f = [x2-x1 for i,x1 in enumerate(e) for j,x2 in enumerate(e) if j == i + 1]

Step 4: Get maximum of f. This is the longest distance between consecutive 1's.

return max(f) if f != [] else 0
