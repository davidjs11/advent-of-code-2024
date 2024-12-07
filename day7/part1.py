# day7 - part1.py

from sys import stdin

def perform_operations(nums, operations):
    total = nums[0]
    i = 1
    for op in operations:
        if op == 'x':
            total *= nums[i]
        else:
            total += nums[i]
        i += 1
    return total

# could have used a recursive function but feelin' lazy today
def test_equation(result, nums):
    for operation in range(0, pow(2, len(nums)-1)):
        operators = ['+' for x in range(len(nums)-1)]
        tmp = operation
        i = 0
        while tmp > 0:
            if tmp % 2 == 1:
                operators[i] = 'x'
            tmp //= 2
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
