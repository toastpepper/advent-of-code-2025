# /usr/bin/env python3

from sys import argv


def area(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)


with open(argv[1] if len(argv) > 1 else "input.txt", "r") as file_in:
    red_tiles = [
        tuple(map(int, line.split(","))) for line in file_in.read().splitlines()
    ]

border = set()
start = red_tiles.index(min(red_tiles))
red_tiles = red_tiles[start + 1 :] + red_tiles[: start + 1]

x1, y1 = red_tiles[-1]

for x2, y2 in red_tiles:
    if x1 == x2:
        border = border.union([(x1, y) for y in range(min(y1, y2) + 1, max(y1, y2))])
    if y1 == y2:
        border = border.union([(x, y1) for x in range(min(x1, x2) + 1, max(x1, x2))])
    x1, y1 = x2, y2

exterior = set()
clockwise = 1 if red_tiles[0][0] == x1 else -1
x1, y1 = red_tiles[-1]

for x2, y2 in red_tiles:
    if y1 < y2:
        # right
        exterior = exterior.union([(x1 - clockwise, y) for y in range(y1, y2 + 1)])
    if y1 > y2:
        # left
        exterior = exterior.union([(x1 + clockwise, y) for y in range(y2, y1 + 1)])
    if x1 < x2:
        # down
        exterior = exterior.union([(x, y1 + clockwise) for x in range(x1, x2 + 1)])
    if x1 > x2:
        # up
        exterior = exterior.union([(x, y1 - clockwise) for x in range(x2, x1 + 1)])

    x1, y1 = x2, y2

exterior.difference_update(border)

# for i in range(max(map(lambda x: x[0], red_tiles)) + 2):
#     for j in range(max(map(lambda x: x[1], red_tiles)) + 2):
#         print(
#             (
#                 "*"
#                 if (i, j) in exterior
#                 else (
#                     "#" if (i, j) in border else ("@" if (i, j) in red_tiles else ".")
#                 )
#             ),
#             end=" ",
#         )
#     print()

pairs = sorted(
    [(t1, t2) for t1 in red_tiles for t2 in red_tiles if t1 < t2],
    key=lambda x: area(*x),
    reverse=True,
)

max_area = area(*pairs[0])
green_area = 0

for p1, p2 in pairs:
    if p1 > p2:
        print("PANIC")
    x1, y1, x2, y2 = *p1, *p2

    in_interior = True
    for x in range(x1 + 1, x2):
        if (x, y1) in exterior or (x, y2) in exterior:
            in_interior = False
            break
    for y in range(min(y1, y2) + 1, max(y1, y2)):
        if (x1, y) in exterior or (x2, y) in exterior:
            in_interior = False
            break

    if in_interior:
        green_area = area(p1, p2)
        break


print("  max area:", max_area)
print("green area:", green_area)
