# day13 - part2.py

from sys import stdin
import numpy as np
import re

# get input
input = []
for lines in stdin:
    input.append(lines)

# solve equations
total = 0
for i in range(0, len(input)+1):
    # button A
    if (i % 4 == 0):
        pattern = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
        for p in pattern.findall(input[i]):
            ax = int(p[0])
            ay = int(p[1])
    # button B
    if (i % 4 == 1):
        pattern = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
        for p in pattern.findall(input[i]):
            bx = int(p[0])
            by = int(p[1])
    # prize
    if (i % 4 == 2):
        pattern = re.compile(r'Prize: X\=(\d+), Y\=(\d+)')
        for p in pattern.findall(input[i]):
            px = int(p[0]) + 10000000000000
            py = int(p[1]) + 10000000000000
    # newline (solve)
    if (i % 4 == 3):
        a = np.array([[ax, bx], [ay, by]], dtype=int)
        c = np.array([px, py], dtype=int)
        sol = np.linalg.solve(a, c)
        sol = [int(round(x)) for x in sol]
        if (sol[0]*ax + sol[1]*bx)==px and (sol[0]*ay + sol[1]*by)==py:
            total += 3*sol[0]+sol[1]

print(f"total: {total}")
