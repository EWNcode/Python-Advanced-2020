"""
Play around with a stack. You will be given an integer N representing the number of elements to push into the stack,
an integer S representing the number of elements to pop from the stack and finally an integer X, an element that you
should look for in the stack. If it's found, print "True" on the console. If it isn't, print the smallest element
currently present in the stack.

"""

def solve_stack(nums, st):
    s = nums[1]
    x = nums[2]


    for i in range(int(s)):
        st.pop()

    if x in st:
        return True
    elif len(st) > 0:
        return sorted(st)[0]
    else:
        return 0


tests = [
    [
        '5 2 13',
        '1 13 45 32 4',
    ],
    [
        '4 1 666',
        '420 69 13 666',
    ],
]


#[print(solve_stack(nums.split(), s.split())) for [nums, s] in tests]

print(solve_stack(input().split(),input().split()))