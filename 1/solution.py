# /usr/bin/env python3

from sys import argv

file_in = open(argv[1] if len(argv) > 1 else "input.txt", "r")
rotations = file_in.readlines()

dial = 50
zeros = 0
overflows = 0


for r in rotations:
    old = dial

    if r[0] == "R":
        dial += int(r[1:])
        if dial % 100 == 0:
            overflows -= 1
    else:
        dial -= int(r[1:])
        if old % 100 == 0:
            overflows -= 1

    if dial % 100 == 0:
        zeros += 1

    overflows += abs(dial // 100 - old // 100)

overflows += zeros

print(f"        password: {zeros}")
print(f"updated password: {overflows}")


file_in.close()
