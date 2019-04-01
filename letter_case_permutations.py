from itertools import product

# Whenever I find a letter, replace it with both its upper- and lowercase forms. Otherwise, leave the digit.

expand_S = [
[x.lower(),x.upper()] \
if x not in string.digits \
else [x] \
for x in list(S)
]

# Create all products of those letters and digits.

ultra_list = product(*expand_S)

# Recreate them as strings.

all_strings = [''.join(s) for s in ultra_list]

return all_strings
