from utils.puzzle_input import get_dummy_input, get_input


#puzzle_input: str = get_dummy_input()
puzzle_input: str = get_input(year=2025, day=11)
connections: list[str] = puzzle_input.splitlines()

nodes = {}
for c in connections:
    origin = c[:3]
    dest = c[4:].strip().split()
    nodes[origin] = dest

start = 'you'
end = 'out'
visited = set()

def dfs(node, visited):
    res = 0
    if node == end:
        return 1

    for dest in nodes[node]:
        if dest in visited:
            continue
        visited.add(dest)
        res += dfs(dest, visited)
        visited.remove(dest)

    return res

print(dfs(start, visited))
