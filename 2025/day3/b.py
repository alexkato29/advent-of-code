from utils.puzzle_input import get_dummy_input, get_input

#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=3)
banks = puzzle_input.split("\n")

N_BATTERIES = 12
res = 0

for bank in banks:
	batteries = [0] * N_BATTERIES
	for i in range(len(bank)):
		val = int(bank[i])
		start = max(0, N_BATTERIES - (len(bank) - i))
		for j in range(start, len(batteries)):
			if val > batteries[j]:
				batteries[j] = val
				batteries[j + 1:] = [0] * (len(batteries) - j - 1)
				break
	res += int("".join(map(str, batteries)))

print(res)
