"""
Using list comprehension write a program that receives numbers separated by comma and space ", " and prints all the
positive, negative, even and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number
"""

numbers = list(map(int, input().split(', ')))

print(f'Positive: {", ".join(map(str, [num for num in numbers if num >= 0]))}\n\
Negative: {", ".join(map(str, [num for num in numbers if num < 0]))}\n\
Even: {", ".join(map(str, [num for num in numbers if num % 2 == 0]))}\n\
Odd: {", ".join(map(str, [num for num in numbers if num % 2 == 1]))}\n')
