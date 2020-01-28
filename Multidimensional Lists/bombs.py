"""
You will be given a square matrix of integers, each integer separated by a single space, and each row on a new line.
Then on the last line of input you will receive indexes - coordinates to several cells separated by a single space,
in the following format: row1,column1  row2,column2  row3,column3… On those cells there are bombs. You must detonate
every bomb, one by one in the order they were given. When a bomb explodes it deals damage equal to its own integer
value, to all the cells around it (in every direction and in all diagonals). One bomb can't explode more than once
and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterwards, print the matrix with all its cells
(including the dead ones).
"""


def read_matrix():
    rows_count = int(input())
    matrix = []
    for i in range(rows_count):
        matrix.append(list(map(int, input().split())))
    return matrix


def explosions(matrix):
    possitions = input().split()
    for possition in possitions:
        row, col = list(map(int, possition.split(',')))
        bomb = matrix[row][col]
        if not bomb <= 0:
            if row - 1 >= 0:
                if matrix[row - 1][col] > 0:
                    matrix[row - 1][col] -= bomb
                if col - 1 >= 0 and matrix[row - 1][col - 1] > 0:
                    matrix[row - 1][col - 1] -= bomb
                if col + 1 < len(matrix) and matrix[row - 1][col + 1] > 0:
                    matrix[row - 1][col + 1] -= bomb

            if col - 1 >= 0 and matrix[row][col -1] > 0:
                matrix[row][col - 1] -= bomb
            if col + 1 < len(matrix) and matrix[row][col + 1] > 0:
                matrix[row][col + 1] -= bomb

            if row + 1 < len(matrix):
                if matrix[row + 1][col] > 0:
                    matrix[row + 1][col] -= bomb
                if col - 1 >= 0 and matrix[row + 1][col - 1] > 0:
                    matrix[row + 1][col - 1] -= bomb
                if col + 1 < len(matrix) and matrix[row + 1][col + 1] > 0:
                    matrix[row + 1][col + 1] -= bomb
            matrix[row][col] = 0
    return matrix


matrix = read_matrix()
matrix_after_explosions = explosions(matrix)

count = 0
sum = 0
for row in range(len(matrix_after_explosions)):
    for col in range(len(matrix_after_explosions)):
        if matrix_after_explosions[row][col] > 0:
            count += 1
            sum += matrix_after_explosions[row][col]

new_line = '\n'

print(f'Alive cells: {count}\nSum: {sum}\n{new_line.join([" ".join(map( str, row))for row in matrix_after_explosions])}')