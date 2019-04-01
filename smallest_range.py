Step 1: Find all indices of char C in string S.

C_indices = [i for i,x in enumerate(S) if x == C]

Step 2: Find minimum distance, compare index of each letter with all indices of char C.

answer = [min(abs(i-i_c) for i_c in C_indices) for i,x in enumerate(S)]
