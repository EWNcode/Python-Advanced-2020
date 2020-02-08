"""
You will receive a list of numbers. Round every number and print the total sum multiplied by the length of the initial
list.

"""

def round_nums_and_sum(numbers):
    return sum(round(num) for num in numbers)*len(numbers)

numbers = list(map(float, input().split()))

print(round_nums_and_sum(numbers))