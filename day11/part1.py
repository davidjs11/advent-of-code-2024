# day11 - part1.py

# get the number of digits of a number
def num_digits(num):
    i = 0
    while num > 0:
        num = int(num/10)
        i += 1
    return i

# apply the specified rules
def apply_rules(stone):
    # rule 1 -> 0 becomes 1
    if stone == 0:
        return 1

    # rule 2 -> nums with even number of digits split in half
    if (num_digits(stone) % 2) == 0:
        n = pow(10, num_digits(stone)/2)
        return [int(stone / n), int(stone % n)]

    # rule 3 -> multiply by 2024
    return stone * 2024


# get input
stones = [int(x) for x in input().split(' ')]

# blink 25 times
for x in range(0, 25):
    new_stones = []

    # apply rules
    for stone in stones:
        result = apply_rules(stone)
        if type(result) == int:
            new_stones.append(result)
        else:
            for x in result:
                new_stones.append(x)
    stones = new_stones.copy()

print(f"total: {len(new_stones)}")
