# day8 - part2.py

from sys import stdin

# check if position is inside map
def inside_map(i, j, map):
    return (0 <= i < len(map)) and (0 <= j < len(map[0]))

# find the antinodes for a given frequency
def find_antinodes(map, freq, antinodes):
    frequencies = []
    # get rest of the frequencies in the map
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == freq:
                frequencies.append((j, i))

    # calculate antinodes
    for i in range(0, len(frequencies)):
        for j in range(i, len(frequencies)):
            if i == j:
                continue
            freqA = frequencies[i]
            freqB = frequencies[j]

            antinodeA = [0, 0]
            antinodeA[0] = freqA[0] + int(freqA[0] - freqB[0])
            antinodeA[1] = freqA[1] + int(freqA[1] - freqB[1])

            antinodeB = [0, 0]
            antinodeB[0] = freqB[0] + int(freqB[0] - freqA[0])
            antinodeB[1] = freqB[1] + int(freqB[1] - freqA[1])

            if inside_map(antinodeA[1], antinodeA[0], map):
                antinodes.add((antinodeA[0], antinodeA[1]))
            if inside_map(antinodeB[1], antinodeB[0], map):
                antinodes.add((antinodeB[0], antinodeB[1]))

def find_t_antinodes(map, freq, antinodes):
    frequencies = []
    # get rest of the frequencies in the map
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == freq:
                frequencies.append((j, i))

    # calculate antinodes
    total = 0
    for i in range(0, len(frequencies)):
        for j in range(i, len(frequencies)):
            if i == j: continue

            freqA = frequencies[i]
            freqB = frequencies[j]

            # from A to B
            antinode = [freqA[0], freqA[1]]
            while inside_map(antinode[1], antinode[0], map):
                antinodes.add((antinode[0], antinode[1]))
                antinode[0] += freqA[0] - freqB[0]
                antinode[1] += freqA[1] - freqB[1]
                total += 1

            # from B to A
            antinode = [freqB[0], freqB[1]]
            while inside_map(antinode[1], antinode[0], map):
                antinodes.add((antinode[0], antinode[1]))
                antinode[0] += freqB[0] - freqA[0]
                antinode[1] += freqB[1] - freqA[1]
                total += 1
    return total

# get input
map = []
for line in stdin:
    map.append(line.split("\n")[0])

# calculate antinodes for the input
calculated = set()
antinodes = set()
antinode_map = map.copy()
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] != '.' and map[i][j] not in calculated:
            # find_antinodes(map, map[i][j], antinodes)
            find_t_antinodes(map, map[i][j], antinodes)
            calculated.add(map[i][j])

print(f"total: {len(antinodes)}")
