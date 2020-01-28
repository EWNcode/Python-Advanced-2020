"""
Write a program which reads a string matrix from the console and performs certain operations with its elements. User
input is provided in a similar way like in the problems above - first you read the dimensions and then the data. Your
program should then receive commands in format: "swap row1 col1 row2c col2" where row1, row2, col1, col2 are
coordinates in the matrix. For a command to be valid, it should start with the "swap" keyword along with four
valid coordinates (no more, no less). You should swap the values at the given coordinates (cell [row1, col1] with
cell [row2, col2]) and print the matrix at each step (thus you'll be able to check if the operation was performed
correctly). If the command is not valid (doesn't contain the keyword "swap", has fewer or more coordinates entered or
the given coordinates do not exist), print "Invalid input!" and move on to the next command. Your program should finish
when the string "END" is entered.

"""

def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for i in range(rows_count):
        matrix.append(input().split())
    return (matrix, rows_count, columns_count)

def matrix_shuffling(matrix, rows_count, columns_count):
    bad_input = 'Invalid input!'
    while True:
        command = input()
        if command == 'END':
            break

        command = command.split()
        if command[0] == 'swap' and len(command) == 5:
            (row1, col1, row2, col2) = map(int, command[1:])

            if (row1 + row2 < rows_count*2) and (col1 + col2 < columns_count*2):
                first_element = matrix[row1][col1]
                second_element = matrix[row2][col2]
                new_matrix = []
                for row in range(rows_count):
                    new_matrix.append([])
                    for cols in range(columns_count):
                        if row1 == row and cols == col1:
                            new_matrix[row].append(second_element)
                        elif row2 == row and cols == col2:
                            new_matrix[row].append(first_element)
                        else:
                            new_matrix[row].append(matrix[row][cols])
                matrix = new_matrix
                new_line = '\n'
                print(new_line.join([' '.join(rows) for rows in matrix]))
            else:
                print(bad_input)
        else:
            print(bad_input)


matrix, rows_count, columns_count = read_matrix()

matrix_shuffling(matrix, rows_count, columns_count)
