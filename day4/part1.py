# day4 - part1.py

from sys import stdin

# character matrix
matrix = []
orders = [[0, 1], [0, -1], [1, 0], [-1, 0],
          [1, 1], [1, -1], [-1, 1], [-1, -1]]
string = "XMAS"

# get value in a given position, checking if correct
def get_position(i, j):
    if 0 <= i < len(matrix[0]) and 0 <= j < len(matrix):
        return matrix[i][j]

# get character matrix from stdin
for line in stdin:
    matrix.append(line.replace("\n", ""))

# iterate matrix
total = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        # if the character is not 'G', skip
        if get_position(i, j) != string[0]:
            continue

        # check every possible order
        for order in orders:
            # new indexes and counter
            count = 0
            new_i = i
            new_j = j

            # while characters are equal, increment counter
            while count < len(string) and get_position(new_i, new_j) == string[count]:
                new_i += order[0]
                new_j += order[1]
                count += 1

            # if counter equals to the length, count one more occurence
            if count == len(string):
                total += 1

print(f"total: {total}")
