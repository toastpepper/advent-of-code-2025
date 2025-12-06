# /usr/bin/env python3

from sys import argv

file_in = open(argv[1] if len(argv) > 1 else "input.txt", "r")
lines = [line.strip() for line in file_in.readlines()]
break_ind = lines.index("")

fresh_ranges = [tuple(map(int, r.split("-"))) for r in lines[:break_ind]]
available = list(map(int, lines[break_ind + 1 :]))

fresh = set()
all_fresh = set()

for item in available:
    for lo, hi in fresh_ranges:
        if item in range(lo, hi + 1):
            fresh.add(item)

fresh_ranges.sort(key=lambda x: x[0])
merged_ranges = []

for lo, hi in fresh_ranges:
    if len(merged_ranges) and lo <= merged_ranges[-1][1]:
        merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], hi))
    else:
        merged_ranges.append((lo, hi))

total_fresh = len(merged_ranges)

for lo, hi in merged_ranges:
    total_fresh += hi - lo

num_fresh = len(fresh)

print("fresh items:", num_fresh)
print("  fresh ids:", total_fresh)

file_in.close()
