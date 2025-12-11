# /usr/bin/env python3

from sys import argv
import z3

with open(argv[1] if len(argv) > 1 else "input.txt", "r") as file_in:
    machines = [line.split() for line in file_in.readlines()]


for i, m in enumerate(machines):
    l = [c == "#" for c in m[0][1:-1]]
    b = [[int(n) for n in b[1:-1].split(",")] for b in m[1:-1]]
    j = [int(n) for n in m[-1][1:-1].split(",")]
    machines[i] = (l, b, j)

light_steps = 0
joltage_steps = 0
for light_target, buttons, joltage_target in machines:
    min_steps = None
    for i in range(2 ** len(buttons)):
        selection = set()

        for j in range(len(buttons)):
            if (i >> j) % 2:
                selection.add(j)

        lights = [False] * len(light_target)

        # press buttons
        for ind in selection:
            for light in buttons[ind]:
                lights[light] = not lights[light]

        if lights == light_target:
            steps = len(selection)
            if min_steps is None:
                min_steps = steps
            else:
                min_steps = min(steps, min_steps)
    light_steps += min_steps

    presses = z3.IntVector("x", len(buttons))
    s = z3.Solver()
    s.add([x >= 0 for x in presses])
    # each joltage must equal the sum of presses for buttons that include it
    for i, joltage in enumerate(joltage_target):
        to_press = []
        for j, button in enumerate(buttons):
            if i in button:
                to_press.append(presses[j])
        s.add(z3.Sum(to_press) == joltage)

    for i in range(1000):
        s.push()
        s.add(z3.Sum(presses) == i)
        if s.check() == z3.sat:
            joltage_steps += i
            break
        s.pop()


print("  light steps:", light_steps)
print("joltage steps:", joltage_steps)
