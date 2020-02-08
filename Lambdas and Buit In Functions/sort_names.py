"""
Write a program that receives a list of names, separated by space and prints the names sorted in descending order.

"""

def sort_names(names):
    return sorted(names, reverse=True)

names = input().split()
print(' '.join(sort_names(names)))