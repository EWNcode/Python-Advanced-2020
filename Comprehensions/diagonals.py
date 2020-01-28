"""
Using nested list comprehension write a program that reads NxN matrix, finds its diagonals, prints them
and their sum as shown below.

"""


def read_matrix(splitter):
    rows_count = int(input())
    matrix = []
    for i in range(rows_count):
        matrix.append(list(map(int, input().split(splitter))))
    return matrix


def find_diagonals(matrix):
    n = len(matrix)
    first_diagonal = [matrix[i][i] for i in range(n)]
    second_diagonal = [matrix[i][n - i - 1] for i in range(n)]
    print(f'First diagonal: {", ".join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}')
    print(f'Second diagonal: {", ".join(map(str,second_diagonal))}. Sum: {sum(second_diagonal)}')


matrix = read_matrix(', ')
find_diagonals(matrix)