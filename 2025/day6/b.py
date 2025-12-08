from utils.puzzle_input import get_dummy_input, get_input


def parse_cols(rows: list[str]) -> list[list[int]]:
	vals = []
	temp = []
	for c in range(len(rows[0])):
		val = ""
		for r in range(len(rows)):
			if rows[r][c] != " ":
				val += rows[r][c]
		if val:
			temp.append(int(val))
		else:
			vals.append(temp)
			temp = []
	vals.append(temp)
	return vals

#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=6)

rows = puzzle_input.split("\n")
operations = rows.pop().split()
vals = parse_cols(rows)

results = [col[0] for col in vals]

for c in range(len(vals)):
	for r in range(1, len(vals[c])):
		if operations[c] == "*":
			results[c] *= vals[c][r]
		else:
			results[c] += vals[c][r]

print(sum(results))
