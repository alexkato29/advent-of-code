from utils.puzzle_input import get_dummy_input, get_input, split_lines


puzzle_input = get_input(year=2025, day=2)
ranges = puzzle_input.split(",")

res = 0

for r in ranges:
	start, end = r.split("-")
	for n in range(int(start), int(end) + 1):
		s = str(n)
		l = len(s)
		for j in range(1, len(s) // 2 + 1):
			if l % j != 0:
				continue
			if s == s[:j] * (l // j):
				res += n
				break

print(res)
