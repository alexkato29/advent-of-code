from utils.puzzle_input import get_dummy_input, get_input


puzzle_input: str = get_input(year=2025, day=1)
instructions: list[str] = puzzle_input.splitlines()

pos: int = 50
res: int = 0

for i in instructions:
    if i[0] == "L":
        pos -= int(i[1:])
    else:
        pos += int(i[1:])
    pos = pos % 100
    if pos == 0:
        res += 1

print(res)
