from utils.puzzle_input import get_dummy_input, get_input


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=7)
grid = puzzle_input.split("\n")
for r in grid:
	r = list(r)

beams = set()
for i in range(len(grid[0])):
	if grid[0][i] == "S":
		beams.add(i)
		break

res = 0
for row in range(2, len(grid), 2):
	updates = []
	for col in range(len(grid[row])):
		if grid[row][col] == "^" and col in beams:
			beams.remove(col)
			res += 1
			l = col - 1
			r = col + 1
			if l >= 0:
				updates.append(l)
			if r < len(grid[r]):
				updates.append(r)
	for u in updates:
		beams.add(u)

print(res)
