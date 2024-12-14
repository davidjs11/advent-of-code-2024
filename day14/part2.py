# day14 - part2.py

# thanks reddit user u/Ak23l for the idea, although
# it's not fully correct, it works for some inputs
# such as mine

from sys import stdin
import re

# get input
robots = []
speeds = []
for line in stdin:
    pattern = re.compile(r'p\=(-?\d+),(-?\d+) v\=(-?\d+),(-?\d+)')
    robot = []
    for x in pattern.findall(line):
        for y in x:
            robot.append(int(y))
    robots.append([robot[0], robot[1]])
    speeds.append([robot[2], robot[3]])

size_x = 101
size_y = 103
seconds = 0
while True:
    seconds += 1

    # move robots
    for i in range(0, len(robots)):
        robots[i][0] = (robots[i][0] + speeds[i][0]) % size_x
        robots[i][1] = (robots[i][1] + speeds[i][1]) % size_y

    # get grid
    grid = []
    for i in range(0, size_x):
        grid.append([0 for j in range(0, size_y)])

    for robot in robots:
        grid[robot[0]][robot[1]] += 1

    # if none overlap, it's the tree
    tree = True
    for i in range(0, size_x):
        for j in range(0, size_y):
            if grid[i][j] > 1:
                tree = False

    # if found, break
    if tree:
        print(f"total {seconds}")
        break
