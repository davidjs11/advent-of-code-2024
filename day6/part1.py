# day6 - part1.py

from sys import stdin

map = []

def new_pos(posx, posy, direction):
    if 0 <= posy < len(map) and 0 <= posx < len(map[0]):
        posx += direction[0]
        posy += direction[1]

        if inside_map(posx, posy) and map[posy][posx] == '#':
            posx -= direction[0]
            posy -= direction[1]
            direction = turn(direction)
            posx += direction[0]
            posy += direction[1]

    return posx, posy, direction

def turn(direction: list):
    newdirection = direction.copy()
    tmp = newdirection[0]
    newdirection[0] = -newdirection[1]
    newdirection[1] = tmp
    return newdirection

def inside_map(posx, posy):
    return 0 <= posy < len(map) and 0 <= posx < len(map[0])

if __name__ == "__main__":
    posx = 0
    posy = 0

    # get map
    for line in stdin:
        map.append(line.replace("\n", ""))
        find = map[posy].find('^')
        if find != -1:
            posx = find
        else:
            posy += 1

    # get positions
    direction = [0, -1]
    while inside_map(posx, posy):
        map[posy] = map[posy][:posx] + 'X' + map[posy][posx+1:]
        posx, posy, direction = new_pos(posx, posy, direction)

    print(f"total: {sum(row.count('X') for row in map)}")
