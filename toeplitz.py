# Step 1. Get starter values.

starters = [(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])) if i == 0 or j == 0]

# Step 2. For each point in starter list, create list of associated diagonal values.

diag = [[(point[0]+i,point[1]+i) for i in range(0,min(len(matrix)-point[0],len(matrix[0])-point[1]))] for point in starters]

# Step 3. For each list of associated diagonal points, list the corresponding matrix value.

diag_vals = [[matrix[points[0]][points[1]] for points in diag_set] for diag_set in diag]

# Step 4. Make a set of each list (so only unique values are shown).
# If set is not singleton (length > 1), then all values in diag set are not the same.

equal_diagonals = [len(set(list_vals)) for list_vals in diag_vals]

toeplitz = len(set(equal_diagonals))

return toeplitz == 1
