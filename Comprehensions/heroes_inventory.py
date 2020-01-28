"""
Using comprehension write a program that receives some hero names, items that need to be added in their inventory
(item name and item cost) and then prints for each hero the total amount of items and the total cost of them.

"""

players = {x: [[], 0] for x in input().split(', ')}

while True:
    data = input()
    if data == 'End':
        break
    data = data.split('-')
    if data[1] not in players[data[0]][0]:
        players[data[0]][0].append(data[1])
        players[data[0]][1] += int(data[2])

{print(f'{k} -> Items: {len(v[0])}, Cost: {v[1]}') for k,v in players.items()}





