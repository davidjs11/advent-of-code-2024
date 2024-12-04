# day3 - part1.py

import re
from sys import stdin

total = 0
for memory in stdin:
    # use regex to find mul(a,b) operations
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    ops = pattern.findall(memory)

    # multiply and add each occurrence
    for op in ops:
        a, b = op
        print(f"{a} * {b} = {int(a)*int(b)}")
        total += int(a) * int(b)

print(f"total: {total}")
