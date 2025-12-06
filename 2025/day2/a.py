from utils.puzzle_input import get_dummy_input, get_input, split_lines


puzzle_input = get_input(year=2025, day=2)
ranges = puzzle_input.split(",")

res = 0

for r in ranges:
	start, end = r.split("-")
	for n in range(int(start), int(end) + 1):
		s = str(n)
		if s[0: len(s) // 2] == s[len(s) // 2:]:
			res += n

print(res)
