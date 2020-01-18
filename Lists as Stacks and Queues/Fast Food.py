"""
You have a fast food restaurant and most of the food that you're offering is previously prepared. You need to know if
you will have enough food to serve lunch to all your customers. Write a program that checks the orders' quantity.
You also want to know the client with the biggest order for the day, because you want to give him a discount the next
time he comes. First, you will be given the quantity of the food that you have for the day (an integer number). Next,
you will be given a sequence of integers, each representing the quantity of an order. Keep the orders in a queue. Find
the biggest order and print it. You will begin servicing your clients from the first one that came. Before each order,
check if you have enough food left to complete it. If you have, remove the order from the queue and reduce the amount
of food you have. If you succeeded in servicing all your clients, print:

"Orders complete".
 If not, print:
"Orders left: {order1} {order2} .... {orderN}".

"""

from collections import deque


def quantity_solver(food_quantity, orders):
    orders = deque(orders)
    biggest_order = sorted(map(int, orders))[-1]
    orders_left = deque()

    while len(orders) > 0:
        current = int(orders.popleft())
        if current > food_quantity:
            orders_left.append(current)
        food_quantity -= current

    if orders_left:
        return f'{biggest_order}\nOrders left: {" ".join(map(str, orders_left))}'
    return f'{biggest_order}\nOrders complete'


tests = [
    [
        '348',
        '20 54 30 16 7 9',
    ],
    [
        '499',
        '57 45 62 70 33 90 88 76 80 9',
    ],
]

[print(quantity_solver(int(food_quantity), orders.split())) for [food_quantity, orders] in tests]
