class Solution:
    def peakIndexInMountainArray(self, A):
        
	# Zip up list with itself, offset by 1. This enables us to compare pairwise values.
	diff_list = zip(A,A[1:])
	
	# Find the pair of values in diff_list such that diff < 0. This means we found the mountain. Return the INDEX, not the values.

        diff = [i for i,x in enumerate(diff_list) if x[1]-x[0] < 0]
        return diff[0]
