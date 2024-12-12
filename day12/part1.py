# day12 - part1.py

from sys import stdin
import copy

# get a plant given its position
def get_plant(map, i, j):
    if (0 <= i < len(map)) and (0 <= j < len(map[0])):
        return map[i][j]
    else:
        return -1

# get the perimeter of a given plant
def perimeter(map, i, j):
    total = 0
    plant = get_plant(map, i, j)
    
    around = [get_plant(map, i-1, j), get_plant(map, i+1, j),
              get_plant(map, i, j-1), get_plant(map, i, j+1)]

    for x in around:
        if x != plant: total += 1

    return total

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

# solve the perimeter given the position of one of its plants
def solve_perimeter(map, i, j, plant, calculated):
    # base case 1 -> out of map
    if not ((0 <= i < len(map)) and (0 <= j < len(map[0]))):
        return 0

    # base case 2 -> pos is already calculated or not the same type
    current_plant = get_plant(map, i, j)
    if current_plant != plant or (i, j) in calculated:
        return 0

    # recursive call
    else:
        calculated.append((i, j))
        return  solve_perimeter(map, i-1, j, current_plant, calculated) + \
                solve_perimeter(map, i+1, j, current_plant, calculated) + \
                solve_perimeter(map, i, j-1, current_plant, calculated) + \
                solve_perimeter(map, i, j+1, current_plant, calculated) + \
                perimeter(map, i, j)

# get input
map = []
for row in stdin:
    line = []
    for col in row.split('\n')[0]:
        line.append(col)
    map.append(line)

# solve problem
total = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if get_plant(map, i, j) == -1: continue
        plant = get_plant(map, i, j)

        per = solve_perimeter(map, i, j, plant, [])
        area = solve_area(map, i, j, plant)

        total += area*per

print(f"total: {total}")
