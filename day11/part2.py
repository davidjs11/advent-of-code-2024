# day11 - part2.py

from functools import cache

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

# divide and conquer with caching is the best thing ever
@cache
def blink(stone, blinks):
    # base case -> return one stone
    if blinks == 0:
        return 1
    
    # apply rules
    if stone == 0:
        return blink(1, blinks-1)
    elif (num_digits(stone) % 2) == 0:
        n = pow(10, num_digits(stone)/2)
        return blink(int(stone/n), blinks-1) + blink(int(stone%n), blinks-1)
    else:
        return blink(stone * 2024, blinks-1)


# get input
stones = [int(x) for x in input().split(' ')]

# blink 25 times
total = 0
for stone in stones:
    total += blink(stone, 75)

print(f"total: {total}")
