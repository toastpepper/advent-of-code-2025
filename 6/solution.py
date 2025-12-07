#/usr/bin/env python3

from sys import argv

file_in = open(argv[1] if len(argv) > 1 else 'input.txt', 'r')



file_in.close()
