from utils.puzzle_input import get_input


OPTIONS = 100
puzzle_input: str = get_input(year=2025, day=1)
instructions: list[str] = puzzle_input.splitlines()

pos: int = 50
res: int = 0

for i in instructions:
    dist: int = int(i[1:])
    if i[0] == "L":
        inc = -(pos - OPTIONS - dist) // OPTIONS
        if pos == 0:  # Avoid double counting when we started at 0
            inc -= 1
        res += inc
        pos -= dist

    else:
        pos += dist
        inc = pos // OPTIONS        
        res += inc

    pos = pos % OPTIONS

print(res)
