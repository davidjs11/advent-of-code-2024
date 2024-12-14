# day14 - part1.py

from sys import stdin
import re

# get input
robots = []
for line in stdin:
    pattern = re.compile(r'p\=(-?\d+),(-?\d+) v\=(-?\d+),(-?\d+)')
    robot = []
    for x in pattern.findall(line):
        for y in x:
            robot.append(int(y))
    robots.append(robot)

# move robots
size_x = 101
size_y = 103
seconds = 100 
for x in range(0, seconds):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % size_x
        robot[1] = (robot[1] + robot[3]) % size_y

# count how many robots are in cuadrants
quadrant = [0, 0, 0, 0]
for robot in robots:
    if robot[0] < int(size_x/2):
        if robot[1] < int(size_y/2):
            quadrant[0] += 1
        elif robot[1] > int(size_y/2):
            quadrant[1] += 1
    elif robot[0] > int(size_x/2):
        if robot[1] > int(size_y/2):
            quadrant[2] += 1
        elif robot[1] < int(size_y/2):
            quadrant[3] += 1

total = 1
for x in quadrant:
    total *= x

print(f"total: {total}")
