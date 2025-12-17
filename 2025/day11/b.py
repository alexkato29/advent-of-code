from functools import cache
from utils.puzzle_input import get_dummy_input, get_input


#puzzle_input: str = get_dummy_input()
puzzle_input: str = get_input(year=2025, day=11)
connections: list[str] = puzzle_input.splitlines()

nodes = {}
for c in connections:
    origin = c[:3]
    dest = c[4:].strip().split()
    nodes[origin] = dest

start = 'svr'
end = 'out'
visited = set()

@cache
def count_paths(node, has_dac, has_fft):
    if node == end:
        return 1 if has_dac and has_fft else 0

    total = 0
    for dest in nodes[node]:
        new_dac = has_dac or (dest == 'dac')
        new_fft = has_fft or (dest == 'fft')
        total += count_paths(dest, new_dac, new_fft)
    
    return total

print(count_paths(start, False, False))
