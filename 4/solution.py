#/usr/bin/env python3

from sys import argv

def count_neighbors(grid, r, c):
    dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    
    ans = 0
    for dr, dc in dirs:
        ans += (r + dr) in range(len(grid)) and (c + dc) in range(len(grid[r])) and grid[r+dr][c+dc]

    return ans
        

file_in = open(argv[1] if len(argv) > 1 else 'input.txt', 'r')
grid = [list(map(lambda x: x == '@', line.strip())) for line in file_in.readlines()]

accessible_rolls = 0

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell and (count_neighbors(grid, r, c) < 4):
            accessible_rolls += 1

removed = 1
total_removed = 0

while removed > 0:
    removed = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell and (count_neighbors(grid, r, c) < 4):
                removed += 1
                grid[r][c] = False
    total_removed += removed

print('accessible rolls:', accessible_rolls)
print('   rolls removed:', total_removed)

file_in.close()
