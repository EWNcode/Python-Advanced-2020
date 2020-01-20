"""
Play around with a queue. You will be given an integer N representing the number of elements to enqueue (add),
an integer S representing the number of elements to dequeue (remove) from the queue and finally an integer X,
an element that you should look for in the queue. If it is, print "True" on the console.
If it's not print the smallest element currently present in the queue. If there are no elements
in the sequence, print 0 on the console.
"""

from collections import deque

def solve_queue(nums, q):
    s = nums[1]
    x = nums[2]
    q = deque(q)

    for i in range(int(s)):
        q.popleft()

    if x in q:
        return True
    elif len(q) > 0:
        return sorted(q)[0]
    else:
        return 0

tests = [
    [
        '5 2 32',
        '1 13 45 32 4',
    ],
    [
        '4 1 666',
        '666 69 13 420',
    ],
    [
        '3 3 90',
        '90 0 90',
    ],
]


[print(solve_queue(nums.split(), q.split())) for [nums, q] in tests]
