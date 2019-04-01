# Footprint of the stack of cubes on xy plane = length of the flattened list. If given a value of 0, it has no footprint - filter for that.
shadow_x = len([c for vector in grid for c in vector if c > 0])

# Maximum of each array (for given x-coordinate) = shadow cast on xz plane.
shadow_y = sum([max(vector) for vector in grid])

# Like shadow_y, but for the yz plane. Do things component-wise.
shadow_z = sum([max([vector[i] for vector in grid]) for i in range(len(grid))])

return shadow_x + shadow_y + shadow_z
