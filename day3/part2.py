import re
from sys import stdin

total = 0
calculate = True
for memory in stdin:
    # use regex to find mul(a,b) operations and do()/don't()
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    ops = re.findall(pattern, memory)

    # multiply and add each occurrence
    for op in ops:
        # check operation type
        if op == 'don\'t()':
            calculate = False
        elif op == 'do()':
            calculate = True
        else:
            if calculate:
                a, b = op.replace("mul(","").replace(")","").split(',')
                print(f"{a} * {b} = {int(a)*int(b)}")
                total += int(a) * int(b)

print(f"total: {total}")
