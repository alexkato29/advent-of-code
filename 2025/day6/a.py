from utils.puzzle_input import get_dummy_input, get_input, split_lines


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=6)
rows = puzzle_input.split("\n")

operations = rows.pop().split()
vals = [list(map(int, line.split())) for line in rows]

results = vals[0]

for i in range(1, len(vals)):
	for j in range(len(vals[i])):
		if operations[j] == "*":
			results[j] *= vals[i][j]
		else:
			results[j] += vals[i][j]

print(sum(results))
