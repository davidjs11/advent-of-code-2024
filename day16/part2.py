# day16 - part2.py

# NOT DONE! i have lots of exams and i'll continue this part when i'm less busy :-(

from sys import stdin
import heapq

# directions: east, north, west, south
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# check if given position is in map
def inmap(i, j, map):
    return (0 <= i < len(map)) and (0 <= j < len(map[0]))

# get map
map = []
for line in stdin:
    row = []
    for x in line[:-1]:
        row.append(x)
    map.append(row)

# get position of start and goal
start = (0, 0)
goal = (0, 0)
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 'S':
            start = (i, j)
        if map[i][j] == 'E':
            goal = (i, j)

# dijkstra's algorithm
def dijkstra(map, start, goal):
    rows, cols = len(map), len(map[0])
    pq = []

    # (cost, (y, x, direction))
    heapq.heappush(pq, (0, (start[0], start[1], 0)))

    visited = set()
    min_cost = float('inf')

    while pq:
        # get node
        cost, (y, x, direction) = heapq.heappop(pq)

        # if node has been visited, stop
        if (y, x, direction) in visited: continue

        # if not, add it
        visited.add((y, x, direction))

        # if goal has been reached
        if (y, x) == goal:
            min_cost = min(min_cost, cost)
            continue

        # move forward
        new_y, new_x = y + directions[direction][0], x + directions[direction][1]
        if inmap(new_y, new_x, map) and map[new_y][new_x] != '#':
            heapq.heappush(pq, (cost + 1, (new_y, new_x, direction)))

        # rotate left
        new_direction = (direction + 1) % 4
        heapq.heappush(pq, (cost + 1000, (y, x, new_direction)))

        # rotate right
        new_direction = (direction - 1) % 4
        heapq.heappush(pq, (cost + 1000, (y, x, new_direction)))

    return min_cost

# solve!
result = dijkstra(map, start, goal)
print(f"total: {result}")
