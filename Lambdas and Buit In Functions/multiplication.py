"""
You will receive a number and a list of numbers. Multiply each number with the initial number and print the result.
"""

def multiply_to_main_number(number, list_nums):
    result = []
    for num in list_nums:
        result.append(num*number)
    return ' '.join(map(str, result))

number = int(input())

list_nums = list(map(int, input().split()))

print(multiply_to_main_number(number, list_nums))