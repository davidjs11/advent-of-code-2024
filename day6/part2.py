# day6 - part2.py

from sys import stdin

def new_pos(posx, posy, direction, map):
    if 0 <= posy < len(map) and 0 <= posx < len(map[0]):
        posx += direction[0]
        posy += direction[1]

        if inside_map(posx, posy, map) and map[posy][posx] == '#':
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

def inside_map(posx, posy, map):
    return 0 <= posy < len(map) and 0 <= posx < len(map[0])

def check_loop(posx, posy, direction, map):
    # get original position
    x = posx
    y = posy

    # obstacle position
    obsx = posx + direction[0]
    obsy = posy + direction[1]
    if not inside_map(obsx, obsy, map):
        return False

    # place obstacle
    newmap = map.copy() 
    newmap[obsy] = newmap[obsy][:obsx] + '#' + newmap[obsy][obsx+1:]

    # get new position
    newdirection = direction.copy()
    posx, posy, newdirection = new_pos(posx, posy, newdirection, newmap)

    # iterate until arriving at the same position
    it = 0
    while (posx != x or posy != y) and it < len(map)*len(map[0]):
        newmap[posy] = newmap[posy][:posx] + 'X' + newmap[posy][posx+1:]
        posx, posy, newdirection = new_pos(posx, posy, newdirection, newmap)
        if not inside_map(posx, posy, newmap):
            break
        it += 1

    return (posx == x and posy == y)

if __name__ == "__main__":
    posx = 0
    posy = 0

    # get map
    map = []
    for line in stdin:
        map.append(line.replace("\n", ""))
        find = map[posy].find('^')
        if find != -1:
            posx = find
        else:
            posy += 1

    total = 0
    total_loops = 0
    direction = [0, -1]
    while inside_map(posx, posy, map):
        if check_loop(posx, posy, direction, map):
            total_loops += 1
        posx, posy, direction = new_pos(posx, posy, direction, map)
        if not inside_map(posx, posy, map):
            break

    print(f"total: {total_loops}")
