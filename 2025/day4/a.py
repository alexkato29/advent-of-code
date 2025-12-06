from typing import Tuple

from utils.puzzle_input import get_dummy_input, get_input, split_lines


DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]  # No (0, 0)

def in_bounds(x: int, y: int, dim: Tuple[int, int]) -> bool:
	return 0 <= x < dim[0] and 0 <= y < dim[1]

#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=4)
grid = puzzle_input.split("\n")
for r in range(len(grid)):
	grid[r] = list(grid[r])
dim = (len(grid[0]), len(grid))

res = 0
for r in range(len(grid)):
	for c in range(len(grid[r])):
		if grid[r][c] != "@":
			continue

		count = 0
		for x, y in DIRECTIONS:
			new_r = r + x
			new_c = c + y
			if in_bounds(new_r, new_c, dim) and grid[new_r][new_c] == "@":
				count += 1

		if count < 4: 
			res += 1

print(res)
