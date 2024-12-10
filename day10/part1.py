# day10 - part1.py

from sys import stdin

# get point in map given its position
def position(i, j, map):
    if (0 <= i < len(map)) and (0 <= j < len(map[0])):
        return map[i][j]

# bfs algorithm :-)
def find_path(i, j, map):
    nodes = [[i, j, 0]]
    height = 0
    paths = []
    while nodes:
        new_nodes = []
        new_nodes.append([nodes[0][0]-1, nodes[0][1], nodes[0][2]])
        new_nodes.append([nodes[0][0]+1, nodes[0][1], nodes[0][2]])
        new_nodes.append([nodes[0][0], nodes[0][1]-1, nodes[0][2]])
        new_nodes.append([nodes[0][0], nodes[0][1]+1, nodes[0][2]])
        for node in new_nodes:
            if position(node[0], node[1], map) == node[2] + 1:
                new_node = [node[0], node[1], node[2]+1]
                if new_node[2] == 9:
                    if new_node not in paths:
                        paths.append(new_node)
                nodes.append(new_node)
        nodes.pop(0)
    return len(paths)

# get map
map = []
for line in stdin:
    row = []
    for point in line.split('\n')[0]:
        row.append(int(point))
    map.append(row)

# find trailheads
trailheads = []
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == 0:
            trailheads.append((i, j))

# find paths from the trailheads
total = 0
for trailhead in trailheads:
    total += find_path(trailhead[0], trailhead[1], map)

print(f"total: {total}")
