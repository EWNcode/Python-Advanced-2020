"""
You own a fashion boutique and you receive a delivery once a month in a huge box, which is full of clothes. You have
to arrange them in your store, so you take the box and start from the last piece of clothing on the top of the pile
to the first one at the bottom. Use a stack for the purpose. Each piece of clothing has its value (an integer). You
have to sum their values, while you take them out of the box. You will be given an integer representing the capacity
of a rack. While the sum of the clothes is less than the capacity, keep summing them.  If the sum becomes equal to
the capacity you have to take a new rack for the next clothes, if there are any left in the box. If it becomes greater
than the capacity, don't add the piece of clothing to the current rack and take a new one. In the end, print how many
racks you have used to hang all of the clothes.

"""

def racks_solver(clothes, rack_size):

    current_size = 0
    racks_counter = 0
    while len(clothes) > 0:

        current_cloth = int(clothes.pop())
        current_size += current_cloth
        if current_size > rack_size:
            racks_counter += 1
            clothes.append(current_cloth)
            current_size = 0
        elif current_size == rack_size:
            racks_counter += 1
            current_size = 0
        elif not clothes:
            racks_counter += 1
    return racks_counter


tests = [
    [
        '5 4 8 6 3 8 7 7 9',
        '16',
    ],
    [
        '1 7 8 2 5 4 7 8 9 6 3 2 5 4 6',
        '20',
    ],
]

[print(racks_solver(clothes.split(), int(rack_size))) for [clothes, rack_size] in tests]
