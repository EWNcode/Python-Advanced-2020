"""
Write a program that prints a set of elements. On the first line you will receive two numbers - n and m, which
represent the lengths of two separate sets. On the next n + m lines you will receive n numbers, which are the
numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear
in both of them and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}

"""
from collections import deque

def set_intersection(set_a, set_b):
    return '\n'.join(set_a & set_b)



#tests = [
#        '4 3',
#        [
#            '1',
#            '3',
#            '5',
#            '7',
#            '3',
#            '4',
#            '5',
#        ],
#]
#
#(nm, numbers) = [x for x in tests]
#n = int(nm[0])
#m = int(nm[-1])
#numbers = deque(numbers)

n, m = [int(x) for x in input().split()]
numbers = deque([input() for x in range(n+m)])

set_a = set()
set_b = set()

[set_a.add(numbers[x]) for x in range(n)]
[numbers.popleft() for _ in range(n)]
[set_b.add(numbers[x]) for x in range(m)]
print(set_intersection(set_a, set_b))