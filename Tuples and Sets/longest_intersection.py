"""
Write a program that finds the longest intersection. You will be given a number N. On the next N lines you will be
given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". Find the intersection of
these two ranges and save the longest one of all N intersections. At the end print the numbers that are included in
the longest intersection and its length in the format: "Longest intersection is {longest_intersection} with length
{length_longest_intersection}"
Note: in each 2 ranges there will always be intersection. If there are two equal intersections, print the first one.
"""

def solve(n, ranges_list):

    result = None
    for i in range(n):
        current_range = ranges_list[i].split('-')
        ll = []
        for y in range(len(current_range)):
            a, b = map(int, current_range[y].split(','))
            ll.append([])
            for z in range(a, b+1):
                ll[y].append(z)
        current = set(ll[0]) & set(ll[-1])
        if result:
            if result < len(current):
                result = len(current)
                best = current
        else:
            result = len(current)
            best = current

    return f'Longest intersection is [{", ".join(map(str, best))}] with length {result}'


tests = [
    [
        '3',
        [
            '0,3-1,2',
            '2,10-3,5',
            '6,15-3,10',
        ],
    ],
    [
        '5',
        [
            '0,10-2,5',
            '3,8-1,7',
            '1,8-2,4',
            '4,7-2,5',
            '1,10-2,11',
        ],
    ]
]

[print(solve(int(n), ranges_list)) for [n, ranges_list] in tests]