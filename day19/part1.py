# day19 - part1.py

from sys import stdin
import functools

towels = []

# recursive function for solving each design
@functools.cache
def solve(design):
    if (len(design) == 0): 
        return True

    results = []
    for p in towels:
        if design[:len(p)] == p:
            results.append(solve(design[len(p):]))

    for x in results:
        if x == True:
            return True
    return False

# get input towels
for line in stdin:
    if line == '\n': break
    towels = [x for x in line.split('\n')[0].split(', ')]

# get input designs
designs = []
for line in stdin:
    designs.append(line[:-1])

# solve!
total = 0
for design in designs:
    total += solve(design)
print(f"total: {total}")
