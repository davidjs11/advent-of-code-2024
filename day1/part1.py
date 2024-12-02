diff = 0
listA = []  # left list
listB = []  # right list

# obtain both lists
try:
    while True:
        itemA, itemB = input().split("   ")
        listA.append(int(itemA))
        listB.append(int(itemB))
except EOFError:
    pass

# calculate the difference between the shortest number on each list
while len(listA) > 0:
    diff += abs(min(listA) - min(listB))
    listA.remove(min(listA))
    listB.remove(min(listB))

print(diff)
