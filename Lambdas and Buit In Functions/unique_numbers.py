"""
You will receive a list of numbers. Round the numbers, print the min and max and multiply the numbers by 3. Print only
the unique numbers in ascending order separated by space.

"""


def unique_numbers(numbers):
    result = ''
    numbers = [round(num) for num in numbers]
    result += str(min(numbers)) + '\n'
    result += str(max(numbers)) + '\n'
    numbers = [num*3 for num in numbers]
    result += ' '.join(map(str, sorted(set(numbers))))
    return result



numbers = list(map(float, input().split()))
print(unique_numbers(numbers))