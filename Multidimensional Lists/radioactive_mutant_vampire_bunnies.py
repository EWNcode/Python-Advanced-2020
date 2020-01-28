"""
Browsing through GitHub, you come across an old JS Basics teamwork game. It is about very nasty bunnies that multiply
extremely fast. There's also a player that has to escape from their lair. You really like the game, so you decide to
port it to Python because that's your language of choice. The last thing that is left is the algorithm that decides
if the player will escape the lair or not.
First, you will receive a line holding integers N and M, which represent the rows and columns in the lair. Then you
receive N strings that can only consist of ".", "B", "P". The bunnies are marked with "B", the player is marked with
"P", and everything else is free space, marked with a dot ".". They represent the initial state of the lair. There
will be only one player. Then you will receive a string with commands such as LLRRUUDD - where each letter represents
the next move of the player (Left, Right, Up, Down).
After each step of the player, each of the bunnies spread to the up, down, left and right (neighboring cells marked as
"." changes their value to B). If the player moves to a bunny cell or a bunny reaches the player, the player has died.
If the player goes out of the lair without encountering a bunny, the player has won.
When the player dies or wins, the game ends. All the activities for this turn continue (e.g. all the bunnies spread
normally), but there are no more turns. There will be no stalemates where the moves of the player end before he dies
or escapes.
Finally, print the final state of the lair with every row on a separate line. On the last line, print either "dead:
{row} {col}" or "won: {row} {col}". Row and col are the coordinates of the cell where the player has died or the last
cell he has been in before escaping the lair.

"""


def read_matrix():
    (rows_count, columns_count) = map(int,input().split())
    matrix = []
    for i in range(rows_count):
        matrix.append([el for el in input()])
    return matrix


def game_over(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                return False
    return True

def find_bunnies(matrix):
    bunny_rows = []
    bunny_cols = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'B':
                bunny_rows.append(row)
                bunny_cols.append(col)
    return bunny_rows, bunny_cols

def find_player(matrix):
    row_start = None
    col_start = None
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                row_start, col_start = row, col
    return (row_start, col_start)

def increase_bunnies(row,col):
    matrix[row][col] = 'B'
    if col - 1 >= 0:
        matrix[row][col-1] = 'B'
    if col + 1 < len(matrix[0]):
        matrix[row][col+1] = 'B'
    if row + 1 < len(matrix):
        matrix[row+1][col] = 'B'
    if row - 1 >= 0:
       matrix[row-1][col] = 'B'
    return matrix


def game(matrix):
    row, col = find_player(matrix)
    bunny_row, bunny_col = find_bunnies(matrix)
    moves = [move for move in input()]
    check = False
    for move in moves:
        if move == 'U':
            if row-1 < 0:
                row = 0
                matrix[row][col] = '.'
                check = True
                break
            matrix[row][col] = '.'
            matrix[row-1][col] = 'P'
            row -= 1
        elif move == 'D':
            if row+1 >= len(matrix):
                row = len(matrix) - 1
                matrix[row][col] = '.'
                check = True
                break
            matrix[row][col] = '.'
            matrix[row+1][col] = 'P'
            row += 1
        elif move == 'L':
            if col-1 < 0:
                col = 0
                matrix[row][col] = '.'
                check = True
                break
            matrix[row][col] = '.'
            matrix[row][col-1] = 'P'
            col -= 1
        elif move == 'R':
            if col+1 >= len(matrix[0]):
                col = len(matrix[0]) - 1
                matrix[row][col] = '.'
                check = True
                break
            matrix[row][col] = '.'
            matrix[row][col+1] = 'P'
            col += 1
        for i in range(len(bunny_row)):
            row_b = bunny_row[i]
            col_b = bunny_col[i]
            matrix = increase_bunnies(row_b, col_b)
        bunny_row, bunny_col = find_bunnies(matrix)

        if game_over(matrix):
            break
    if check:
        for i in range(len(bunny_row)):
            row_b = bunny_row[i]
            col_b = bunny_col[i]
            matrix = increase_bunnies(row_b, col_b)
        bunny_row, bunny_col = find_bunnies(matrix)

    new_line = '\n'
    if check:
        print(f'{new_line.join(["".join(map(str, row)) for row in matrix])}')
        print(f'won: {row} {col}')

    else:
        print(f'{new_line.join(["".join(map(str, row)) for row in matrix])}')
        print(f'dead: {row} {col}')



matrix = read_matrix()

game(matrix)


"""
4 5
.....
.....
.....
.BP..
LLL
"""