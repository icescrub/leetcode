Step 1. Surround grid with water.

1A. Surround grid with moat of water to the left and right.

for row in grid:
	row.insert(0,0)
	row.insert(len(row),0)

1B. Surround grid with moat of water above and below.

x = [0]*len(grid[0])
grid.insert(0,x)
grid.insert(len(grid),x)

Step 2. Calculate perimeter.

perimeter = 0
valid = slice(1,-1)

surrounding values:
	for row in grid[valid]:
		for i in row[valid]:
			above = grid[i][j-1]
			below = grid[i][j+1]
			left = grid[i-1][j]
			right = grid[i+1][j]
			perimeter += 4 - (above + below + left + right)
			
return perimeter
