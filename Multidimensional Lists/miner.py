"""
We get as input the size of the field in which our miner moves. The field is always a square. After that we will receive
the commands which represent the directions in which the miner should move. The miner starts from position - 's'. The
commands will be: left, right, up and down. If the miner has reached a side edge of the field and the next command
indicates that he has to get out of the field, he must remain on his current possition and ignore the current command.
The possible characters that may appear on the screen are:
* - a regular position on the field.
e - the end of the route.
c  - coal
s - the place where the miner starts
Each time when the miner finds a coal, he collects it and replaces it with '*'. Keep track of the count of the collected
coals. If the miner collects all of the coals in the field, the program stops and you have to print the following
message: "You collected all coals! ({rowIndex}, {colIndex})".
If the miner steps at 'e' the game is over (the program stops) and you have to print the following message:
"Game over! ({rowIndex}, {colIndex})".
If there are no more commands and none of the above cases had happened, you have to print the following message:
"{remainingCoals} coals left. ({rowIndex}, {colIndex})".

"""


def read_matrix():
    rows_count = int(input())
    moves = input().split()
    matrix = []
    for i in range(rows_count):
        matrix.append(input().split())
    return (matrix, moves)


def starting_point(matrix):
    coal_count = 0
    row_start = None
    col_start = None
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 's':
                row_start, col_start = row, col
            elif matrix[row][col] == 'c':
                coal_count += 1
    return (row_start, col_start, coal_count)


def miner_moves(matrix, moves):
    row, col, coal_count = starting_point(matrix)
    check = False
    for move in moves:
        if move == 'left':
            if col-1 >= 0:
                col = col -1
        elif move == 'right':
            if col+1 < len(matrix):
                col = col + 1
        elif move == 'up':
            if row-1 >= 0:
                row = row -1
        elif move == 'down':
            if row+1 < len(matrix):
                row = row + 1

        if matrix[row][col] == 'c':
            coal_count -= 1
            matrix[row][col] = '*'
        elif matrix[row][col] == 'e':
            print(f"Game over! ({row}, {col})")
            check = True
            break

        if coal_count == 0:
            print(f"You collected all coals! ({row}, {col})")
            check = True
            break
    if not check:
        print(f'{coal_count} coals left. ({row}, {col})')





(matrix, moves) = read_matrix()

miner_moves(matrix, moves)