# day2 - part2.py

from sys import stdin

def check_levels(levels):
    # calculate difference between numbers
    diff = []
    for x in range(1, len(levels)):
        diff.append(levels[x]-levels[x-1])

    # condition 1:
    # levels are all increasing or all decreasing
    increasing = (diff[0] > 0)
    bad = False
    for x in range(1, len(levels)-1):
        if increasing != (diff[x] > 0):
            bad = True
            break

    # condition 2:
    # all increases/decreases are between 1 and 3
    if not bad:
        for x in diff:
            if (abs(x) < 1 or abs(x) > 3):
                bad = True
                break

    return not bad

# main function
if __name__ == "__main__":
    safe_count = 0

    for line in stdin:
        # get levels
        levels = []
        for x in line.split(" "):
            levels.append(int(x))

        # check array removing each level
        for x in range(0, len(levels)):
            new_levels = levels.copy()
            new_levels.pop(x)
            if check_levels(new_levels):
                safe_count += 1
                break

    print(f"total: {safe_count}")
