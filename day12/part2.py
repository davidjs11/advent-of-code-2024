# day12 - part2.py

from sys import stdin
import copy

# get a plant given its position
def get_plant(map, i, j):
    if (0 <= i < len(map)) and (0 <= j < len(map[0])):
        return map[i][j]
    else:
        return -1

# solve the area given the position of one of its plants
def solve_area(map, i, j, plant):
    # base case 1 -> out of map
    if not ((0 <= i < len(map)) and (0 <= j < len(map[0]))):
        return 0


    # base case 2 -> not the same type
    current_plant = get_plant(map, i, j)
    if current_plant != plant:
        return 0

    # recursive call
    else:
        map[i][j] = -1
        return  solve_area(map, i-1, j, current_plant) + \
                solve_area(map, i+1, j, current_plant) + \
                solve_area(map, i, j-1, current_plant) + \
                solve_area(map, i, j+1, current_plant) + 1

# solve the sides given the position of one of its plants
# this algorithm took me more than i thought
def solve_sides(map, region):
    region = list(region)
    plant = get_plant(map, region[0][0], region[0][1])

    total = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if (i, j) not in region: continue
            for dir in dirs:
                n = (i+dir[0], j+dir[1])
                m = (-abs(dir[1]), -abs(dir[0]))

                if get_plant(map, n[0], n[1]) != plant:
                    prev = (i+m[0], j+m[1])
                    prevn = (prev[0]+dir[0], prev[1]+dir[1])
                    if prev not in region:
                        total += 1
                    elif get_plant(map, prevn[0], prevn[1]) == plant:
                        total += 1
    return total

# solve the sides given the position of one of its plants
def fill(map, i, j, plant, calculated):
    # base case 1 -> out of map
    if not ((0 <= i < len(map)) and (0 <= j < len(map[0]))):
        return calculated

    # base case 2 -> pos is already calculated or not the same type
    current_plant = get_plant(map, i, j)
    if current_plant != plant or (i, j) in calculated:
        return calculated

    # recursive call
    else:
        calculated.add((i, j))
        fill(map, i-1, j, current_plant, calculated)
        fill(map, i+1, j, current_plant, calculated)
        fill(map, i, j-1, current_plant, calculated)
        fill(map, i, j+1, current_plant, calculated)
    return calculated

# get input
map = []
for row in stdin:
    line = []
    for col in row.split('\n')[0]:
        line.append(col)
    map.append(line)

# solve problem
total = 0
regions = []
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if get_plant(map, i, j) == -1: continue
        plant = get_plant(map, i, j)

        # obtain regions
        region = fill(map, i, j, plant, set())
        sides = 0
        if region not in regions:
            sides = solve_sides(map, region)
            regions.append(region)

        area = solve_area(map, i, j, plant)
        total += area * sides

print(f"total: {total}")
