"""
You have an empty sequence, and you will be given N queries. Each query is one of these three types:
1 – Push the element x into the stack.
2 – Delete the element present at the top of the stack.
3 – Print the maximum element in the stack.
4 – Print the minimum element in the stack.
After you go through all the queries, print the stack in the following format:
"{n}, {n1}, {n2} …, {nn}"

"""


def solve_stack(n, commands):
    st = []

    for i in range(n):
        command = commands[i].split()
        if command[0] == '1':
            st.append(int(command[-1]))
        elif st:
            if command[0] == '2':
                st.pop()
            elif command[0] == '3':
                print(max(st))
            else:
                print(min(st))
    return ', '.join(map(str,st[::-1]))


tests = [
    [
            '9',
        [
            '1 97',
            '2',
            '1 20',
            '2',
            '1 26',
            '1 20',
            '3',
            '1 91',
            '4',
         ]
    ],
    [
            '10',
        [
            '2',
            '1 47',
            '1 66',
            '1 32',
            '4',
            '3',
            '1 25',
            '1 16',
            '1 8',
            '4',
        ]
    ],
]


[print(solve_stack(int(n), commands)) for [n, commands] in tests]
