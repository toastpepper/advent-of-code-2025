# /usr/bin/env python3

from sys import argv

with open(argv[1] if len(argv) > 1 else "input.txt", "r") as file_in:
    machines = [line.split() for line in file_in.readlines()]


for i, m in enumerate(machines):
    l = [c == "#" for c in m[0][1:-1]]
    b = [[int(n) for n in b[1:-1].split(",")] for b in m[1:-1]]
    j = [int(n) for n in m[-1][1:-1].split(",")]
    machines[i] = (l, b, j)

total_steps = 0
for schematic, buttons, _ in machines:
    min_steps = None
    for i in range(2 ** len(buttons)):
        selection = set()

        for j in range(len(buttons)):
            if (i >> j) % 2:
                selection.add(j)

        lights = [False] * len(schematic)

        # press buttons
        for ind in selection:
            for light in buttons[ind]:
                lights[light] = not lights[light]

        if lights == schematic:
            steps = len(selection)
            if min_steps is None:
                min_steps = steps
            else:
                min_steps = min(steps, min_steps)
    total_steps += min_steps
print("light configuration steps:", total_steps)
