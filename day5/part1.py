# day5 - part1.py

from sys import stdin

rules = {}
updates = []
reading_rules = True
total = 0

# read rules
for line in stdin:
    # if newline is reached, start reading updates
    if line == "\n":
        break

    a, b = [int(x) for x in line.split('|')]
    if a in rules:
        rules[a].append(b)
    else:
        rules[a] = []
        rules[a].append(b)

# read updates
for line in stdin:
    update = [int(x) for x in line.split(',')]
    updates.append(update)

for update in updates:
    # check order
    correct = True
    for i in range(0, len(update)):
        for j in range(0, i):
            a = update[i]
            b = update[j]
            if a in rules and b in rules[a]:
                correct = False
        for j in range(i+1, len(update)):
            a = update[i]
            b = update[j]
            if a in rules and b not in rules[a]:
                correct = False

    # add middle numbers
    if correct:
        total += update[int(len(update)/2)]

print(f"total: {total}")
