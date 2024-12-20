# day20 - part2.py

from sys import stdin

def inmap(i, j, map):
    return (0 <= i < len(map)) and (0 <= j < len(map[0]))

def manhattan(i1, j1, i2, j2):
    return abs(i1-i2)+abs(j1-j2)

def find_neighbours(i, j, map, distance):
    result = []
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if 1 < manhattan(i, j, y, x) <= distance:
                result.append((y, x))
    return result

def get_circle(pos, radius):
    points = set()
    for i in range(radius + 1):
        x, y = (i, radius - i)
        points.update([(x, y), (-x, -y), (x, -y), (-x, y)])
    for point in points:
        yield tuple(x + y for x, y in zip(pos, point))

# get input
map = []
for line in stdin:
    row = []
    for x in line[:-1]:
        row.append(x)
    map.append(row)

# search start and end
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == 'E': end = (i, j)
        if map[i][j] == 'S': start = (i, j)

# get path from start to end
nodes = [(start[0], start[1], 0)]
visited = []
all = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while nodes:
    node = nodes[0]
    nodes.pop(0)
    visited.append((node[0], node[1]))
    all.append(node)
    if map[node[0]][node[1]] == 'E': break

    for dir in dirs:
        newnode = (node[0]+dir[0], node[1]+dir[1], node[2]+1)
        if  (newnode[0], newnode[1]) not in visited and \
            inmap(newnode[0], newnode[1], map) and \
            map[newnode[0]][newnode[1]] != '#':
            nodes.append(newnode)
path_from_start = visited.copy()
cost_from_start = all.copy()

# get path from end to start
nodes = [(end[0], end[1], 0)]
visited = []
all = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while nodes:
    node = nodes[0]
    nodes.pop(0)
    if map[node[0]][node[1]] == 'S': break
    visited.append((node[0], node[1]))
    all.append(node)

    for dir in dirs:
        newnode = (node[0]+dir[0], node[1]+dir[1], node[2]+1)
        if  (newnode[0], newnode[1]) not in visited and \
            inmap(newnode[0], newnode[1], map) and \
            map[newnode[0]][newnode[1]] != '#':
            nodes.append(newnode)
path_from_end = visited.copy()
cost_from_end = all.copy()

total = 0
saves = []
calculated = []
for i, j in path_from_start:
    # get neighbours with distance 20
    for rad in range(2, 21):
        neighbours = get_circle((i, j), rad)
        for n in neighbours:
            if n in path_from_end and n not in calculated:
                path = 0
                for x in range(0, len(cost_from_start)):
                    if (cost_from_start[x][0], cost_from_start[x][1]) == (i, j):
                        path += cost_from_start[x][2]
                        break
                path += 2
                for x in range(0, len(cost_from_end)):
                    if (cost_from_end[x][0], cost_from_end[x][1]) == n:
                        path += cost_from_end[x][2]
                        if len(path_from_end)-path > 0:
                            saves.append(len(path_from_end)-path)
                        break
                calculated.append(n)

for x in saves:
    if x >= 100:
        print(x)
        total += 1
print(f"total: {total}")
