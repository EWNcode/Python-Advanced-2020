"""
Write a program that receives a list of strings. Keep the numbers, remove the names and check if the numbers are bigger
than the initial length of the list. Then print the numbers in ascending order

"""

def sort_numbers(data):
    numbers = []
    for strng in data:
        if strng.isdigit() and int(strng) > len(data):
            numbers.append(int(strng))
    return ' '.join(map(str, sorted(numbers)))


data = input().split()

print(sort_numbers(data))