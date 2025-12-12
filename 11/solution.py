# /usr/bin/env python3

from sys import argv
from time import sleep


def top_order(curr, v: set, o: list):
    if curr in v:
        return

    for next in links.setdefault(curr, []):
        top_order(next, v, o)

    v.add(curr)
    o.insert(0, curr)


with open(argv[1] if len(argv) > 1 else "input.txt", "r") as file_in:
    lines = [line.split() for line in file_in.read().splitlines()]

links = dict([(line[0][:-1], line[1:]) for line in lines])


if len(argv) == 1 or argv[-1] == "b":
    num_paths = 0
    s = ["you" if len(argv) == 1 else "svr"]
    # dfs through paths
    while s:
        curr = s.pop()

        if curr == "out":
            num_paths += 1

        s += links.setdefault(curr, [])

    print("         paths:", num_paths)


num_filtered = 0

visited = set()
ordered_nodes = []
top_order("svr", visited, ordered_nodes)

paths_to_node = {"svr": 1}
for i, node in enumerate(ordered_nodes[1:]):
    paths_to_node[node] = sum(
        [
            paths_to_node.setdefault(prev, 0)
            for prev in ordered_nodes[: i + 1]
            if node in links[prev]
        ]
    )
    if node in ("fft", "dac"):
        paths_to_node = {node: paths_to_node[node]}

num_filtered = paths_to_node["out"]

print("filtered paths:", num_filtered)
