# day18 - part1.py

from sys import stdin

# map dimensions
mem_width = 70
mem_height = mem_width

# check if a position is in the map
def inmap(i, j, map):
    return (0 <= i < len(map)) and (0 <= j < len(map[0]))
    
# get memory map
mem = []
for i in range(0, mem_width+1):
    row = []
    for j in range(0, mem_width+1):
        row.append('.')
    mem.append(row)

# get input
count = 1024
for line in stdin:
    if (count > 0):
        i, j = [int(x) for x in line.split(',')]
        mem[i][j] = '#'
        count -= 1

# solve!! (bfs algorithm)
nodes = [(0, 0, 0)]
visited = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while nodes:
    # get node
    node = nodes[0]
    while (node[0], node[1]) in visited:
        nodes.pop(0)
        node = nodes[0]
    visited.append((node[0], node[1]))

    # check if node is a solution
    if node[0] == mem_height and node[1] == mem_width:
        solution = node
        break

    # generate new nodes
    for dir in directions:
        newnode = (node[0]+dir[0], node[1]+dir[1], node[2]+1)
        if not inmap(newnode[0], newnode[1], mem): continue
        if (newnode[0], newnode[1]) in visited: continue
        if mem[newnode[0]][newnode[1]] == '#': continue
        nodes.append(newnode)

    nodes.pop(0)
    
print(f"total: {solution[2]}")
