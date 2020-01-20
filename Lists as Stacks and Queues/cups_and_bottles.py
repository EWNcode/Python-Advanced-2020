"""
You will be given a sequence of integers – each indicating a cup's capacity. After that you will be given another
sequence of integers – a bottle with water in it. Your job is to try to fill up all of the cups. Filling is done by
picking exactly one bottle at a time. You must start picking from the last received bottle and start filling from the
first entered cup. If the current bottle has N water, you give the first entered cup N water and reduce its integer
value by N. When a cup's integer value reaches 0 or less, it gets removed. It is possible that the current cup's value
is greater than the current bottle's value. In that case you pick bottles until you reduce the cup's integer value to 0
 or less. If a bottle's value is greater or equal to the cup's current value, you fill up the cup and the remaining
 water becomes wasted. You should keep track of the wasted litters of water and print it at the end of the program.
If you have managed to fill up all of the cups, print the remaining water bottles, from the last entered – to the
first, otherwise you must print the remaining cups, by order of entrance – from the first entered – to the last.

"""

from collections import deque


def cup_fill(cups, bottles):
    cups = deque(cups)

    waste_water = 0
    result = ''

    while cups:
        if not bottles:
            result += f'Cups: {" ".join(map(str, cups))}\n'
            break
        current_cup = int(cups.popleft())
        while current_cup:
            current_bottle = int(bottles.pop())
            current_cup -= current_bottle

            if current_cup <= 0:
                waste_water += abs(current_cup)
                break
    if bottles:
        result += f'Bottles: {" ".join(map(str, bottles))}\n'
    result += f'Wasted litters of water: {waste_water}'
    return result





tests = [
    [
        '4 2 10 5',
        '3 15 15 11 6',
    ],
    [
        '1 5 28 1 4',
        '3 18 1 9 30 4 5',
    ],
    [
        '10 20 30 40 50',
        '20 11',
    ],
]


[print(cup_fill(cups.split(), bottles.split())) for [cups, bottles] in tests]
