from utils.puzzle_input import get_dummy_input, get_input, split_lines


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=5)
ranges, ingredients = puzzle_input.split("\n\n")

ingredients = ingredients.split("\n")
ranges = ranges.split("\n")

res = 0
for i in ingredients:
	i = i.strip()
	i = int(i)
	for r in ranges:
		start, end = r.split('-')
		start = int(start)
		end = int(end)

		if start <= i <= end:
			res += 1
			break

print(res)

