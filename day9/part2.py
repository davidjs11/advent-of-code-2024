# day9 - part2.py

from sys import stdin

def find_free_space(disk, pos, size):
    enough = False
    while not enough and pos < len(disk):
        # search free space
        while pos < len(disk) and disk[pos] != -1:
            pos += 1
        if pos == len(disk):
            return -1

        # check size
        found = 0
        while pos+found < len(disk) and disk[pos+found] == -1 and found < size:
            found += 1
        if found == size:
            return pos
        else:
            pos += found
    return -1

def find_last_block(disk, pos, id):
    while pos > 0 and disk[pos] != id:
        pos -= 1
    return pos

# get input
input = input()
disk = []
id = 0
ids = []
for i in range(0, len(input)):
    if (i % 2 == 0):
        ids.append(int(input[i]))
        for x in range(0, int(input[i])):
            disk.append(id)
        id += 1
    else:
        for i in range(0, int(input[i])):
            disk.append(-1)

# find last id
last_pos = len(disk)-1
while last_pos >= 0 and disk[last_pos] == -1:
    last_pos -= 1
last_id = disk[last_pos]

# compact disk
while last_id >= 0:

    # find first free position
    free_pos = find_free_space(disk, 0, ids[last_id])
    if free_pos == -1:
        last_id -= 1
        continue

    # find last block that matches last id
    last_pos = find_last_block(disk, len(disk)-1, last_id)

    if free_pos < last_pos:
        for i in range(0, ids[last_id]):
            disk[free_pos] = disk[last_pos]
            disk[last_pos] = -1
            free_pos += 1
            last_pos -= 1

    last_id -= 1

# checksum
total = 0
for i in range(0, len(disk)):
    if disk[i] != -1:
        total += i * disk[i]
print(f"total: {total}")
