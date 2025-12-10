from utils.puzzle_input import get_dummy_input, get_input


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=9)

raw_points = puzzle_input.split("\n")

maxy = 0
points = []
for point in raw_points:
	x, y = point.split(',')
	x = int(x)
	y = int(y)
	maxy = max(maxy, y)
	points.append((x, y))

# We can do this greedily. The best rectangle is necessarily one of two options
# A: The top left-most corner to bottom right-most corner
# B: The bottom left-most corner to top right-most corner
# (Provable by greedy stays ahead)
tl = (-1, -1, float('inf'))
br = (-1, -1, 0)
bl = (-1, -1, float('inf'))
tr = (-1, -1, 0)
for p in points:
	d_tl = p[0] ** 2 + p[1] ** 2
	if d_tl < tl[2]:
		tl = (p[0], p[1], d_tl)
	if d_tl > br[2]:
		br = (p[0], p[1], d_tl)
	
	d_bl = p[0] ** 2 + (p[1] - maxy) ** 2
	if d_bl < bl[2]:
		bl = (p[0], p[1], d_bl)
	if d_bl > tr[2]:
		tr = (p[0], p[1], d_bl)

res = max(
	(abs(tl[0] - br[0]) + 1) * (abs(tl[1] - br[1]) + 1),
	(abs(bl[0] - tr[0]) + 1) * (abs(bl[1] - tr[1]) + 1)
)

print(res)
