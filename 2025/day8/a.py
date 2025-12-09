from collections import defaultdict
from utils.puzzle_input import get_dummy_input, get_input
from utils.union_find import UnionFind


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=8)
raw_points = puzzle_input.split("\n")
points = []
for idx, point in enumerate(raw_points):
	coords = point.split(',')
	points.append((int(coords[0]), int(coords[1]), int(coords[2]), idx))

edges = []
for idx, p in enumerate(points):
	for q in points[idx+1:]:
		d = ((p[0] - q[0]) ** 2) + ((p[1] - q[1]) ** 2) + ((p[2] - q[2]) ** 2)
		edges.append((d, p[3], q[3]))

edges.sort()

union = UnionFind(len(points))
for e in edges[:1000]:
	union.union(e[1], e[2])

circuits = defaultdict(list)
for p in points:
	parent = union.find(p[3])
	circuits[parent].append(p[3])

circuit_sizes = [len(circuit) for circuit in circuits.values()]
circuit_sizes.sort(reverse=True)

print(circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])
