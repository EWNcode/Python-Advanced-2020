"""
You will receive a command and a list of numbers:
If the command is "Odd": Print the sum of the Odd numbers multiplied by the length of the initial list.
If the command is "Even": Print the sum of the Even numbers multiplied by the length of the initial list.

"""

def odd_or_even(command, numbers):
    if command == 'Odd':
        return sum(x for x in numbers if x % 2 == 1)*len(numbers)
    return sum(x for x in numbers if x % 2 == 0) * len(numbers)


command = input()
numbers = list(map(int, input().split()))
print(odd_or_even(command, numbers))