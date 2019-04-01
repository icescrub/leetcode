grid

Step 1: flatten list

flat_list = itertools.chain.from_iterable(grid)

Step 2: identify all surface areas

Outer surface area = 2*all elements in list
Top/bottom surface area = 2*length of the list (1 for each bloc)
inner surface area = 

==============

for each STACK (list in the grid):
	1. first and last pieces are corner pieces *always* (top/bottom of shape)
	2. if i = 0 or i = len(grid), then stack's outer area is 2xheight. Otherwise 1xheight.
	3. compare with height of surrounding stacks. If this stack is higher, add difference in heights to area.
