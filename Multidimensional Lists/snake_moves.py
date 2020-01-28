"""
You are walking in the park and you encounter a snake! You are terrified, and you start running zigzag, so the snake
starts following you.You have a task to visualize the snake's path in a square form. A snake is represented by a string.
The isle is a rectangular matrix of size NxM. A snake starts going down from the top-left corner and slithers its way
down. The first cell is filled with the first symbol of the snake, the second cell is filled with the second symbol,
etc. The snake is as long as it takes in order to fill the stairs completely - if you reach the end of the string
representing the snake, start again at the beginning. After you fill the matrix with the snake's path, you should
print it.
"""
from collections import deque


def read_matrix():
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for i in range(rows_count):
        matrix.append([])
        for y in range(columns_count):
            matrix[i].append(None)
    return (matrix, rows_count, columns_count)


def matrix_snake(matrix, rows_count, columns_count):
    new_line = '\n'
    snake = deque(input())
    snake_name = ''.join(snake)
    for row in range(rows_count):
        if row % 2 == 0:
            for col in range(columns_count):
                if len(snake) == 0:
                    [snake.append(el) for el in snake_name]
                matrix[row][col] = snake.popleft()
            print(''.join(matrix[row]))

        else:
            for col in range(columns_count-1, -1, -1):
                if len(snake) == 0:
                    [snake.append(el) for el in snake_name]
                matrix[row][col] = snake.popleft()
            print(''.join(matrix[row]))
        if len(snake) > 0:
            snake_left = snake.pop() + snake_name
        else:
            snake_left = '' + snake_name
        [snake.append(el) for el in snake_left]


(matrix, rows_count, columns_count) = read_matrix()

matrix_snake(matrix, rows_count, columns_count)