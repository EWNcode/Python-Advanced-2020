def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append([ch for ch in input()])
    return matrix

def find_player(matrix):
    row_start = None
    col_start = None
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                row_start, col_start = row, col
    return (row_start, col_start)


def game(matrix, row, col, string):
    n = int(input())

    for i in range(n):

        command = input()

        if command == 'up':
            if row-1 in range(len(matrix)):
                matrix[row][col] = '-'
                if not matrix[row-1][col] == '-':
                    string += matrix[row-1][col]
                matrix[row-1][col] = 'P'
                row -= 1
            else:
                string = string[:-1]

        elif command == 'down':
            if row+1 in range(len(matrix)):
                matrix[row][col] = '-'
                if not matrix[row+1][col] == '-':
                    string += matrix[row+1][col]
                matrix[row+1][col] = 'P'
                row += 1
            else:
                string = string[:-1]

        elif command == 'left':
            if col-1 in range(len(matrix[0])):
                matrix[row][col] = '-'
                if not matrix[row][col-1] == '-':
                    string += matrix[row][col-1]
                matrix[row][col-1] = 'P'
                col -= 1
            else:
                string = string[:-1]

        elif command == 'right':
            if col+1 in range(len(matrix[0])):
                matrix[row][col] = '-'
                if not matrix[row][col+1] == '-':
                    string += matrix[row][col+1]
                matrix[row][col+1] = 'P'
                col += 1
            else:
                string = string[:-1]

    print(string)
    [print(''.join(row)) for row in matrix]


string = input()
matrix = read_matrix()
row_start, col_start = find_player(matrix)

game(matrix, row_start, col_start, string)