# /usr/bin/env python3

from sys import argv

file_in = open(argv[1] if len(argv) > 1 else "input.txt", "r")
rotations = file_in.readlines()

dial = 50
zeros = 0

for r in rotations:
    dial += int(r[1:]) * (-1 if r[0] == "L" else 1)
    if dial % 100 == 0:
        zeros += 1

print(f"password: {zeros}")


file_in.close()
