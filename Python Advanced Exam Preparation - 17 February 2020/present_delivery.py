def read_matrix():
    (rows_count) = int(input())
    matrix = []
    for i in range(rows_count):
        matrix.append(input().split())
    return matrix

def find_santa(matrix):
    row_start = None
    col_start = None
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'S':
                row_start, col_start = row, col
    return (row_start, col_start)


def good_kids_check(matrix):
    good_kids = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'V':
                good_kids += 1
    return good_kids

def cookie(matrix, row, col, presents, count_happy):
    if (matrix[row][col-1] == 'V' or matrix[row][col-1] == 'X'):
        if matrix[row][col-1] == 'V':
            count_happy += 1
        matrix[row][col-1] = '-'
        presents -= 1

    if (matrix[row][col+1] == 'V' or matrix[row][col+1] == 'X'):
        if matrix[row][col+1] == 'V':
            count_happy += 1
        matrix[row][col+1] = '-'
        presents -= 1

    if (matrix[row-1][col] == 'V' or matrix[row-1][col] == 'X'):
        if matrix[row-1][col] == 'V':
            count_happy += 1
        matrix[row-1][col] = '-'
        presents -= 1

    if (matrix[row+1][col] == 'V' or matrix[row+1][col] == 'X'):
        if matrix[row+1][col] == 'V':
            count_happy += 1
        matrix[row+1][col] = '-'
        presents -= 1

    return (matrix, presents, count_happy)



def santa_moves(matrix, presents, row_start, col_start):
    count_happy_kids = 0
    while presents > 0:
        command = input()
        if command == 'Christmas morning':
            break
        if command == 'up':
            if row_start - 1 >= 0:
                matrix[row_start][col_start] = '-'
                if matrix[row_start-1][col_start] == 'C':
                    matrix[row_start - 1][col_start] = 'S'
                    (matrix, presents, count_happy_kids) = cookie(matrix, row_start-1, col_start, presents, count_happy_kids)
                    row_start = row_start - 1
                    continue
                elif matrix[row_start-1][col_start] == 'V':
                    presents -= 1
                    count_happy_kids += 1
                matrix[row_start-1][col_start] = 'S'
                row_start = row_start-1
        elif command == 'down':
            if row_start + 1 < len(matrix):
                matrix[row_start][col_start] = '-'
                if matrix[row_start + 1][col_start] == 'C':
                    matrix[row_start + 1][col_start] = 'S'
                    (matrix, presents, count_happy_kids) = cookie(matrix, row_start+1, col_start, presents, count_happy_kids)
                    row_start = row_start + 1
                    continue
                elif matrix[row_start+1][col_start] == 'V':
                    presents -= 1
                    count_happy_kids += 1
                matrix[row_start+1][col_start] = 'S'
                row_start = row_start + 1
        elif command == 'left':
            if col_start - 1 >= 0:
                matrix[row_start][col_start] = '-'
                if matrix[row_start][col_start-1] == 'C':
                    matrix[row_start][col_start-1] = 'S'
                    (matrix, presents, count_happy_kids) = cookie(matrix, row_start, col_start-1, presents, count_happy_kids)
                    col_start = col_start - 1
                    continue
                elif matrix[row_start][col_start-1] == 'V':
                    presents -= 1
                    count_happy_kids += 1
                matrix[row_start][col_start-1] = 'S'
                col_start = col_start - 1
        elif command == 'right':
            if col_start + 1 < len(matrix[0]):
                matrix[row_start][col_start] = '-'
                if matrix[row_start][col_start+1] == 'C':
                    matrix[row_start][col_start+1] = 'S'
                    (matrix, presents, count_happy_kids) = cookie(matrix, row_start, col_start+1, presents, count_happy_kids)
                    col_start = col_start + 1
                    continue
                elif matrix[row_start][col_start+1] == 'V':
                    presents -= 1
                    count_happy_kids += 1
                matrix[row_start][col_start+1] = 'S'
                col_start = col_start + 1

    good_kids = good_kids_check(matrix)

    if presents <= 0 and good_kids > 0:
            print("Santa ran out of presents!")

    for row in matrix:
        print(" ".join(row) + ' ')

    if good_kids == 0:
        print(f'Good job, Santa! {count_happy_kids} happy nice kid/s.')
    else:
        print(f'No presents for {good_kids} nice kid/s.')




presents = int(input())
matrix = read_matrix()
row_start, col_start = find_santa(matrix)
santa_moves(matrix, presents, row_start, col_start)