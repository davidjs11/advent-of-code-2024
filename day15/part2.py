# day15 - part2.py

from sys import stdin
import copy

# not fully complete - works for some inputs :-(

# check if pos is in map
def inmap(pos, map):
    return (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[0]))

# check if boxes are movable
def can_move(pos, dir, box, map):
    newpos = [pos[0]+dir[0], pos[1]+dir[1]]
    if not inmap(pos, map): return False
    if not inmap(newpos, map): return False
    obj = map[newpos[0]][newpos[1]]
    if obj == '@': return False
    if obj == '.': return True
    if obj == '#': return False
    if obj == '[' and not box:
        return can_move([newpos[0], newpos[1]], dir, True, map) and can_move([newpos[0], newpos[1]+1], dir, False, map)
    if obj == ']' and not box: 
        return can_move([newpos[0], newpos[1]], dir, True, map) and can_move([newpos[0], newpos[1]-1], dir, False, map)

    return False

# move an object
def move(pos, dir, map):
    newpos = [pos[0]+dir[0], pos[1]+dir[1]]
    obj = map[pos[0]][pos[1]]

    if not inmap(pos, map): return pos
    if not inmap(newpos, map): return pos

    if map[newpos[0]][newpos[1]] == '[':
        if dir[0] != 0:
            if not can_move(newpos, dir, False, map): return pos
        m = copy.deepcopy(map)
        p = move([newpos[0], newpos[1]+1], dir, m)
        if p != [newpos[0], newpos[1]+1] and map[newpos[0]+dir[0]][newpos[1]] != '#':
            move([newpos[0], newpos[1]+1], dir, map)
            move([newpos[0], newpos[1]], dir, map)
    if map[newpos[0]][newpos[1]] == ']':
        if dir[0] != 0:
            if not can_move(newpos, dir, False, map): return pos
        m = copy.deepcopy(map)
        p = move([newpos[0], newpos[1]-1], dir, m)
        if p != [newpos[0], newpos[1]-1] and map[newpos[0]+dir[0]][newpos[1]] != '#':
            move([newpos[0], newpos[1]-1], dir, map)
            move([newpos[0], newpos[1]], dir, map)
    if map[newpos[0]][newpos[1]] == '#':
        return pos
    if map[newpos[0]][newpos[1]] == '.':
        map[pos[0]][pos[1]] = '.'
        map[newpos[0]][newpos[1]] = obj
        return newpos
    return pos

# get map from input
map = []
for line in stdin:
    if line == "\n": break
    map.append(line[:-1])

# get the new map format
newmap = []
for row in map:
    newrow = []
    for obj in row:
        if obj == '#':
            newrow.append('#')
            newrow.append('#')
        elif obj == 'O':
            newrow.append('[')
            newrow.append(']')
        elif obj == '.':
            newrow.append('.')
            newrow.append('.')
        elif obj == '@':
            newrow.append('@')
            newrow.append('.')
    newmap.append(newrow)

map = newmap
    
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
    for row in map:
        for x in row:
            print(x, end="")
        print()
    if dir == (-1, 0):
        print("up")
    if dir == (1, 0):
        print("down")
    if dir == (0, -1):
        print("left")
    if dir == (0, 1):
        print("right")
    submarine = move(submarine, dir, map)

for row in map:
    for x in row:
        print(x, end="")
    print()

# calculate GPS coordinates of boxes
total = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == '[':
            total += 100*i+j

print(f"total: {total}")
