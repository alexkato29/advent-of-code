from utils.puzzle_input import get_dummy_input, get_input


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=7)
puzzle_input = puzzle_input.split("\n")
grid = []
for row in range(len(puzzle_input) - 1, -1, -1):
	grid.append(list(puzzle_input[row]))

dp = [[0] * len(r) for r in grid]
dp[0] = [1] * len(grid[0])

for row in range(1, len(grid)):
	for col in range(len(grid[row])):
		if grid[row][col] == ".":
			dp[row][col] = dp[row - 1][col]
		elif grid[row][col] == "^":
			dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col + 1]
		elif grid[row][col] == "S":
			print(dp[row - 1][col - 1] + dp[row - 1][col + 1])
