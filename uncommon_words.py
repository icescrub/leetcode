from collections import Counter

# Count words in each sentence.

cA = Counter(A.split())
cB = Counter(B.split())

# Only get unique words.

cA_unique = {k:v for k,v in cA.items() if v == 1}
cB_unique = {k:v for k,v in cB.items() if v == 1}

setA = set(cA_unique)
setB = set(cB_unique)

return setA.symmetric_difference(setB)

"""
ALT SOLUTION: Like mine, but moves past filtering for unique values, then casting to sets, then doing a set calculation.

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())
        return [word for word in count if count[word] == 1]
"""
