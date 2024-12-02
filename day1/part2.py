similarity = 0
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

for a in listA:
    similarity += listB.count(a) * a

print(similarity)
