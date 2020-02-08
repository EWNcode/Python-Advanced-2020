"""
You will receive a list of numbers. Remove the positive numbers, sum the negative numbers and print the absolute value.

"""

def remove_positive_and_sum_negative(numbers):
    numbers = [num for num in numbers if num < 0]
    return abs(sum(numbers))

numbers = list(map(int, input().split()))

print(remove_positive_and_sum_negative(numbers))
