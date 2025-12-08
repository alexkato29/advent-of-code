from utils.puzzle_input import get_input


puzzle_input = get_input(year=2025, day=3)
banks = puzzle_input.split("\n")

res = 0

for bank in banks:
	first = 0
	second = 0
	for i in range(len(bank)):
		val = int(bank[i])
		if val > first and (i != len(bank) - 1):
			first = val
			second = int(bank[i + 1])
			continue
		if val > second:
			second = val
	res += 10 * first + second

print(res)
