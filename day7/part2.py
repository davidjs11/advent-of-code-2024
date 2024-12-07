# day7 - part2.py

from sys import stdin

def perform_operations(nums, operations):
    total = nums[0]
    i = 1
    for op in operations:
        if op == 'x':
            total *= nums[i]
        elif op == '+':
            total += nums[i]
        else:
            total = int(str(total)+str(nums[i]))
        i += 1
    return total

def test_equation(result, nums):
    for operation in range(0, pow(3, len(nums)-1)):
        operators = ['+' for x in range(len(nums)-1)]
        tmp = operation
        i = 0
        while tmp > 0:
            if tmp % 3 == 1:
                operators[i] = 'x'
            elif tmp % 3 == 2:
                operators[i] = '||'
            tmp //= 3
            i += 1

        total = perform_operations(nums, operators)
        if total == result:
            return True
    return False

total = 0
for line in stdin:
    result = int(line.split(":")[0])
    nums = [int(x) for x in line.split(":")[1].split(" ")[1:]]
    if test_equation(result, nums):
        total += result

print(f"total: {total}")
