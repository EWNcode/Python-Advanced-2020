"""
Chess is the oldest game, but it is still popular these days. For this task we will use only one chess piece - the
Knight. The knight moves to the nearest square but not on the same row, column, or diagonal. (This can be thought of as
moving two squares horizontally, then one square vertically, or moving one square horizontally then two squares
vertically - i.e. in an "L" pattern.) The knight game is played on a board with dimensions N x N and a lot of chess
knights 0 <= K <= N2. You will receive a board with K for knights and '0' for empty cells. Your task is to remove a
minimum of the knights, so there will be no knights left that can attack another knight.

"""



def read_matrix():
    rows_count = int(input())
    matrix = []
    for i in range(rows_count):
        matrix.append([el for el in input()])
    return (matrix, rows_count)

def moves(r, row, col, element):
    count = 0
    if col - 1 >= 0 and row + 2 < r:
        if matrix[row + 2][col - 1] == element:
            count += 1
    if col - 1 >= 0 and row - 2 >= 0:
        if matrix[row - 2][col - 1] == element:
            count += 1
    if col + 1 < r and row + 2 < r:
        if matrix[row + 2][col + 1] == element:
            count += 1
    if col + 1 < r and row - 2 >= 0:
        if matrix[row - 2][col + 1] == element:
            count += 1
    if row + 1 < r and col - 2 >= 0:
        if matrix[row + 1][col - 2] == element:
            count += 1
    if row + 1 < r and col + 2 < r:
        if matrix[row + 1][col + 2] == element:
            count += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == element:
            count += 1
    if row - 1 >= 0 and col + 2 < r:
        if matrix[row - 1][col + 2] == element:
            count += 1
    return count


def remove_knights(matrix, r):
    element = 'K'
    total_damage = 0
    knight = []
    removed = 0
    while True:
        damage = 0
        for row in range(r):
            for col in range(r):
                if matrix[row][col] == element:
                    damage += moves(r, row, col, element)

                    if damage > total_damage:
                        total_damage = damage
                        knight = [row, col]
                    damage = 0

        if total_damage == 0:
            return removed
        matrix[knight[0]][knight[1]] = '0'
        total_damage = 0
        knight = []
        removed += 1




(matrix, rows_count) = read_matrix()

result = remove_knights(matrix, rows_count)

print(result)

