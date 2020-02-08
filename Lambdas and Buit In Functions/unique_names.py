"""
You will receive a list of numbers. Round the numbers, print the min and max and multiply the numbers by 3. Print only
the unique numbers in ascending order separated by space.

"""

def unique_names(names):
    return sum(len(name) for name in names if name.istitle())


names = input().split()
print(unique_names(names))