"""
Write a program that reads some text from the console and counts the occurrences of each character in it. Print the
results in alphabetical (lexicographical) order.
"""


def letter_count(string):
    d1 = {}
    for i in range(len(string)):
        element = string[i]
        if element not in d1:
            d1[element] = 0
        d1[element] += 1
    d1 = sorted(d1.items(), key=lambda x: x)
    for k,v in d1:
        print(f'{k}: {v} time/s')

tests = [
    'SoftUni rocks',
]

[letter_count(string) for string in tests]
