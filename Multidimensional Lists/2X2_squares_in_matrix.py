"""
Find the count of 2 x 2 squares of equal chars in a matrix.
"""


def read_matrix(splitter):
    (rows_count, columns_count) = map(int, input().split(splitter))
    matrix = []
    for i in range(rows_count):
        matrix.append(input().split(splitter))
    return (matrix, rows_count, columns_count)


def find_squares_in_matrix(matrix, rows_count, columns_count):
    squares = 0
    for i in range(rows_count-1):
        for y in range(columns_count-1):
            if matrix[i][y] == matrix[i][y+1] and\
                    matrix[i][y] == matrix[i+1][y] and\
                    matrix[i][y] == matrix[i+1][y+1]:
                squares += 1
    return squares


(matrix, rows_count, columns_count) = read_matrix(' ')

result = find_squares_in_matrix(matrix, rows_count, columns_count)

print(result)