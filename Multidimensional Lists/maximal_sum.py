"""
Write a program that reads a rectangular integer matrix of size N x M and finds in it the square 
3 x 3 that has maximal sum of its elements.
"""


def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for i in range(rows_count):
        matrix.append(list(map(int, input().split())))
    return (matrix)


def maximum_sum(matrix):
    max_sum = None
    best_matrix = None
    row_count = len(matrix)
    column_count = (len(matrix[0]))
    for i in range(row_count-2):
        for y in range(column_count-2):
            current_sub_matrix = [[matrix[i][y], matrix[i][y+1], matrix[i][y+2]],
                                    [matrix[i+1][y], matrix[i+1][y+1], matrix[i+1][y+2]],
                                    [matrix[i+2][y], matrix[i+2][y+1], matrix[i+2][y+2]]]

            current_sub_matrix_sum = sum(sum(row) for row in current_sub_matrix)

            if max_sum:
                if max_sum < current_sub_matrix_sum:
                    max_sum = current_sub_matrix_sum
                    best_matrix = current_sub_matrix

            else:
                max_sum = current_sub_matrix_sum
                best_matrix = current_sub_matrix

    return (max_sum, best_matrix)


matrix = read_matrix()

the_sum, sub_matrix = maximum_sum(matrix)

new_line = '\n'
print(f'Sum = {the_sum}\n{new_line.join([" ".join(map(str, row)) for row in sub_matrix])}')




