# /usr/bin/env python3

from sys import argv
from functools import reduce


def str_at(s, i):
    if i >= len(s):
        return ""
    return s[i]


with open(argv[1] if len(argv) > 1 else "input.txt", "r") as file_in:
    lines = file_in.read().splitlines()

rows = []
ops = lines[-1].split()

for line in lines[:-1]:
    rows.append(line.split())

cols = list(zip(*rows))

total = 0
corrected = 0

cols = [list(map(int, col)) for col in cols]

for op, col in zip(ops, cols):
    total += sum(col) if op == "+" else reduce(lambda x, y: x * y, col)

print("   answer total:", total)
print("corrected total:", corrected)
