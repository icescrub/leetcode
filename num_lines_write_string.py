import string
from collections import Counter

Step 1. Relate letters in alphabet to their widths.

dict_w = dict(zip(string.ascii_lowercase,widths))

Step 2. Count number of letters in S.

counter = Counter(S)

Step 3. Relate widths of letters to their frequencies in S.

dict_w = Dictionary of widths:
	a --> w(a)
	b --> w(b)

counter = Dictionary of frequencies:
	a --> count(a)
	b --> count(b)

map_wc = Dictionary mapping the two:
	w(a) --> c(a)
	w(b) --> c(b)

map_wc = [(dict_w[key],counter[key]) for key in counter.keys()]

Step 4. Multiply these and sum them.

width_total = sum((w[0]*w[1] for w in map_wc))

Step 5: # of lines

width_total//100 + 1

Step 6: width of last line

Step 6A. Take string, convert to its letters, replace letters with widths.

rev_dict_w = {v:k for k,v in dict_w.items()}
	a --> w(a)
	b --> w(b)

width_of_S = list(rev_dict_w[letter] for letter in S)

Step 6B: Now find disjoint sublists such that sum(sublist) <= 100.

CURRENT IDEA: accumulate function (10,10,10,...) --> (10,20,30,...). Take values for which <= 100. keep doing that until you have lists.

j = range(len(x))
i = 0

while j < len(x):
	y = max(j for j in range(len(x)) if sum(x[i:j]) <= 100)
	i = y


================

from bisect import bisect
from itertools import accumulate
from math import ceil

class Solution:
    def numberOfLines(self, widths, S):

# replace letters with their widths.

x = [widths[ord(letter)-97] for letter in S]

# get the growing width.

accumulated = list(accumulate(x))

# Need to find VALUES where the accumulated list needs to be partitioned. Every 100 lines, including the two end points.

bisection_values = [100*i for i in range(ceil(accumulated[-1]/100) + 1)]

# find the INDICES where the accumulated list will be partitioned at.

bisection_points = [bisect(accumulated,v) for v in bisection_values]

all_lists = [x[i1:i2] for i1,i2 in zip(bisection_points,bisection_points[1:])]

"""
def numberOfLines(width,S):
	x = [widths[ord(letter)-97] for letter in S]
	accumulated = list(accumulate(x))
	bisection_values = [100*i for i in range(ceil(accumulated[-1]/100) + 1)]        
	bisection_points = [bisect(accumulated,v) for v in bisection_values]
	all_lists = [x[i1:i2] for i1,i2 in zip(bisection_points,bisection_points[1:])]
	return bisection_values,bisection_points,all_lists
	# return len(all_lists), sum(all_lists[-1])


[7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
"zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
"""
