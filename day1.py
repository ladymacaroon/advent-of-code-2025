import sys
from functools import reduce
import itertools

lines = map(str.strip, sys.stdin.readlines())

def sign(line):
    match line[:1]:
        case 'L': return -1
        case 'R': return 1

def number(line):
    return int(line[1:])

numbers = map(lambda line: sign(line) * number(line), lines)

steps = itertools.accumulate(numbers, lambda acc, n: (acc + n) % 100, initial=50)
total = 0

for x in steps:
    if x == 0:
        total += 1

print(total)
