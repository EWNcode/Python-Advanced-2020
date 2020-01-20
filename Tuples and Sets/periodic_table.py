"""
Write a program that keeps all the unique chemical elements. On the first line you will be given a number n - the
count of input lines that you are going to receive. On the next n lines, you will be receiving chemical compounds,
separated by a single space. Your task is to print all the unique ones on a separate lines (order does not matter):
"""


def unique_elements(n, elements):
    l1 = []
    for i in range(n):
        current = elements[i].split()
        l1.extend(current)
    s = set(l1)
    return '\n'.join(s)

tests = [
        [
            '4',
            [
                'Ce O',
                'Mo O Ce',
                'Ee',
                'Mo',
            ],
        ],
        [
            '3',
            [
                'Ge Ch O Ne',
                'Nb Mo Tc',
                'O Ne',
            ],
        ],
]

#[print(unique_elements(int(x), y)) for [x, y] in tests]

n = int(input())
elements = [input() for _ in range(n)]
print(unique_elements(n, elements))


