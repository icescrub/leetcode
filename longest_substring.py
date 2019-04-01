import string

class Solution:
    def lengthOfLongestSubstring(self, s):

# For all letters in the alphabet, we're going to winnow down substrings of the given string.

for current_letter in string.ascii_lowercase:
	letter_locs = [i for i,x in enumerate(s) if x == current_letter]
	
	len(letter_locs) == 1:
		return s
	len(letter_locs) == 2:
		
		max(letter_locs[0], letter_locs[0]+1 - letter_locs[1], letter_locs[1]+1 - len(s))
		
