"""
Create a function called even_odd that can receive different amount of numbers and a command at the end. The command
can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
"""


def even_odd(*args):
    key = args[-1]
    args = args[:-1]
    x = 0 if key == 'even' else 1
    return [num for num in args if num % 2 == x]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
