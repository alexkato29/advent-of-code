from utils.puzzle_input import get_dummy_input, get_input, split_lines


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=5)
input_ranges, ingredients = puzzle_input.split("\n\n")

input_ranges = input_ranges.split("\n")
ranges = []
for i in range(len(input_ranges)):
	start, end = input_ranges[i].split('-')
	start = int(start)
	end = int(end)
	ranges.append((start, end))
ranges.sort()

distinct_ranges = []

for start, end in ranges:
	if not distinct_ranges:
		distinct_ranges.append((start, end))
		continue
	if start > distinct_ranges[-1][1]:
		distinct_ranges.append((start, end))
	elif end > distinct_ranges[-1][1]:
		orig_start, orig_end = distinct_ranges.pop()
		distinct_ranges.append((orig_start, end))

res = 0
for r in distinct_ranges:
	res += r[1] - r[0] + 1

print(res)
