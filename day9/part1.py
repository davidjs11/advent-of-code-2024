# day9 - part1.py

from sys import stdin

# get input
input = input()
disk = []
id = 0
for i in range(0, len(input)):
    if (i % 2 == 0):
        for i in range(0, int(input[i])):
            disk.append(id)
        id += 1
    else:
        for i in range(0, int(input[i])):
            disk.append(-1)

# compact disk
free_pos = 0
last_pos = len(disk)-1
while free_pos < len(disk) and disk[free_pos] != -1:
    free_pos += 1

# find last block
while last_pos >= 0 and disk[last_pos] == -1:
    last_pos -= 1

# repeat until disk is defragmented
while last_pos >= free_pos:
    disk[free_pos] = disk[last_pos]
    disk[last_pos] = -1
    # find first free position
    while free_pos < len(disk) and disk[free_pos] != -1:
        free_pos += 1

    # find last block
    while last_pos >= 0 and disk[last_pos] == -1:
        last_pos -= 1

# checksum
total = 0
for i in range(0, free_pos):
    total += i * disk[i]
print(f"total: {total}")
