"""
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).

"""

def read_matrix(splitter):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split(splitter))))
    return (matrix, n)


def find_diagonal_difference(matrix, n):
    primary_sum = 0
    secondary_sum = 0

    for i in range(int(n)):
        primary_sum += matrix[i][i]
        secondary_sum += matrix[i][n-1-i]
    return abs(primary_sum - secondary_sum)


(matrix, n) = read_matrix(' ')

result = find_diagonal_difference(matrix, n)

print(result)
