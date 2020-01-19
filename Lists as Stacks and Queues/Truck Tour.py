"""
Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to (N−1) (both
inclusive). You have two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol
that petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump (kilometers).
Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol
pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck
will stop at each of the petrol pumps. The truck will move one kilometer for each liter of the petrol.

"""

from collections import deque


def where_to_start(petrol_pumps):
    petrol_pumps = deque(petrol_pumps)
    petrol_in_truck = 0
    current = 0
    counter = 0

    while len(petrol_pumps) > 0:
        pump = petrol_pumps.popleft().split()
        petrol_in_truck += (int(pump[0]) - int(pump[-1]))
        if petrol_in_truck < 0:
            current = counter + 1
            petrol_in_truck = 0
        counter += 1
    return current


tests = [
    [
        '3',
        [
            '1 5',
            '10 3',
            '3 4',
        ]
    ],
]

[print(where_to_start(petrol_pumps)) for [n, petrol_pumps] in tests]

