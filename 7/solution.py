# /usr/bin/env python3

from sys import argv

with open(argv[1] if len(argv) > 1 else "input.txt", "r") as file_in:
    lines = file_in.read().splitlines()


rows = [list(map(lambda x: x != ".", row)) for row in lines]
beams = set([rows[0].index(True)])
particles = list(map(int, rows[0]))
rows = rows[1:]

num_splits = 0

for splitters in rows:
    new_beams = set()
    for beam in beams:
        if splitters[beam]:
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
            num_splits += 1
        else:
            new_beams.add(beam)
    beams = new_beams

    new_particles = [0] * len(particles)
    for i, ct in enumerate(particles):
        if splitters[i]:
            new_particles[i - 1] += ct
            new_particles[i + 1] += ct
        else:
            new_particles[i] += ct
    particles = new_particles

num_timelines = sum(particles)

print("   split count:", num_splits)
print("timeline count:", num_timelines)
