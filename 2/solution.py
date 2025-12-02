#/usr/bin/env python3

from sys import argv

def get_factors(n):
    return set(filter(lambda x: n % x == 0, range(2,n+1)))

file_in = open(argv[1] if len(argv) > 1 else 'input.txt', 'r')
ranges = [tuple(r.split('-')) for r in file_in.read().strip().split(',')]

pair_sum = 0
chain_sum = 0

for lo, hi in ranges:
    invalid_ids = set()
    doubled_ids = set()

    lo_factors = get_factors(len(lo))
    hi_factors = get_factors(len(hi)).difference(lo_factors)

    for chain_length in lo_factors:
        unit_length = len(lo) // chain_length

        for unit in range(int(lo[:unit_length]), int(str(min(int(hi),10**len(lo)-1))[:unit_length])+1):
            id = int(str(unit)*chain_length)
            if id in range(int(lo),int(hi)+1):
                invalid_ids.add(id)
                if chain_length == 2:
                    doubled_ids.add(id)
                # print(id)

    for chain_length in hi_factors:
        unit_length = len(hi) // chain_length
        for unit in range(int(('1'+'0'*(len(hi)-1))[:unit_length]),int(hi[:unit_length])+1):
            id = int(str(unit)*chain_length)
            if id in range(int(lo),int(hi)+1):
                invalid_ids.add(id)
                if chain_length == 2:
                    doubled_ids.add(id)
                # print(id)
    
    chain_sum += sum(invalid_ids)
    pair_sum += sum(doubled_ids)

print(f" id sum: {pair_sum}")
print(f"new sum: {chain_sum}")

file_in.close()

