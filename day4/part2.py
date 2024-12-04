# day4 - part2.py

from sys import stdin

# character matrix
matrix = []

# get value in a given position, checking if correct
def get_position(i, j):
    if 0 <= i < len(matrix[0]) and 0 <= j < len(matrix):
        return matrix[i][j]

# get the 4 corner characters from one character
def get_corners(i, j):
    result = ""
    result += str(get_position(i-1, j-1))
    result += str(get_position(i-1, j+1))
    result += str(get_position(i+1, j-1))
    result += str(get_position(i+1, j+1))
    return result

# get character matrix from stdin
for line in stdin:
    matrix.append(line.replace("\n", ""))

# iterate matrix
total = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        # if character is 'A', check corners
        if get_position(i, j) == 'A':
            corners = get_corners(i, j)

            # check if it's one of the 4 possible orders
            if  corners == "MSMS" or \
                corners == "SMSM" or \
                corners == "MMSS" or \
                corners == "SSMM":
                total += 1

print(f"total: {total}")
