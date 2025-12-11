# /usr/bin/env python3

from sys import argv
from math import dist, prod

with open(argv[1] if len(argv) > 1 else "input.txt", "r") as file_in:
    boxes = [tuple(map(int, box.split(","))) for box in file_in.read().splitlines()]

num_links = 10 if len(argv) > 1 else 1000

links = sorted(
    [(i, j) for i in range(len(boxes)) for j in range(len(boxes)) if i < j],
    key=lambda x: dist(boxes[x[0]], boxes[x[1]]),
)

circuits = [set([i]) for i in range(len(boxes))]
for i, (a, b) in enumerate(links):
    for circuit in circuits:
        if a in circuit:
            a_circ = circuit
        if b in circuit:
            b_circ = circuit
    if a_circ != b_circ:
        circuits.append(a_circ.union(b_circ))
        circuits.remove(a_circ)
        circuits.remove(b_circ)
    if i == num_links - 1:
        circ_prod = prod(map(len, sorted(circuits, key=len, reverse=True)[:3]))
    if len(circuits) == 1:
        x_prod = boxes[a][0] * boxes[b][0]
        break

print("circuit product:", circ_prod)
print("      x product:", x_prod)
