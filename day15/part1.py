# day15 - part1.py

from sys import stdin

# check if pos is in map
def inmap(pos, map):
    return (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[0]))

# move an object
def move(pos, dir, map):
    newpos = [pos[0]+dir[0], pos[1]+dir[1]]
    obj = map[pos[0]][pos[1]]

    if not inmap(pos, map): return pos
    if not inmap(newpos, map): return pos

    if map[newpos[0]][newpos[1]] == 'O':
        move(newpos, dir, map)
    if map[newpos[0]][newpos[1]] == '#':
        return pos
    if map[newpos[0]][newpos[1]] == '.':
        map[pos[0]] = map[pos[0]][:pos[1]] + '.' + map[pos[0]][pos[1]+1:]
        map[newpos[0]] = map[newpos[0]][:newpos[1]] + obj + map[newpos[0]][newpos[1]+1:]
        return newpos
    return pos

# get map from input
map = []
for line in stdin:
    if line == "\n": break
    map.append(line[:-1])
    
# get directions from input
directions = []
for line in stdin:
    for x in line[:-1]:
        if x == '^': directions.append((-1, 0))
        if x == 'v': directions.append((1, 0))
        if x == '<': directions.append((0, -1))
        if x == '>': directions.append((0, 1))

# search submarine position
submarine = [0, 0]
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == '@':
            submarine = [i, j]

# move!
for dir in directions:
    submarine = move(submarine, dir, map)

# calculate GPS coordinates of boxes
total = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == 'O':
            total += 100*i+j

print(f"total: {total}")
