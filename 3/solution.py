#/usr/bin/env python3

from sys import argv

def get_joltage(bank, n):
    if n < 2:
        return 0

    start = 0
    batteries = ''

    for end in range(len(bank) - n + 1, len(bank) + 1):
        battery = max(*bank[start:end])
        start += bank[start:end].find(battery) + 1

        batteries += battery
    
    return int(batteries)


file_in = open(argv[1] if len(argv) > 1 else 'input.txt', 'r')
banks = [l.strip() for l in file_in.readlines()]

output = 0
boosted = 0

for bank in banks:
    output += get_joltage(bank, 2)
    boosted += get_joltage(bank, 12)


print('        output joltage:', output)
print('boosted output joltage:', boosted)

file_in.close()
