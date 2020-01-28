"""
Using comprehension write a program that finds all the amount of all items in a bunker and their average quantity. On
the first line you will be given all the categories of items in the bunker, then you will be given a number (n). On the
next "n" lines you will be given items in the following format:
"{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}".
Store that information, you will need it later. After you received all the inputs, print the total amount of items
(sum the quantities) in the format: "Count of items: {count}". After that print the average quality of all items in
the format: "Average quality: {quality - formatted to the second digit}". Finally, print all of the categories with the
items on separate lines in it in the format: "{category} -> {item1}, {item2}…"

"""


categories = {x: [] for x in input().split(', ')}

n = int(input())
total_quality = 0
total_quantity = 0
for _ in range(n):
    data = input().split(' - ')
    category = data[0]
    kind = data[1]
    quantity = int(data[-1].split(';')[0].split(':')[-1])
    quality = int(data[-1].split(';')[-1].split(':')[-1])

    categories[category].append(kind)
    total_quality += quality
    total_quantity += quantity



print(f'Count of items: {total_quantity}\nAverage quality: {total_quality/len(categories):.2f}')

{print(f'{k} -> {", ".join(v)}') for k,v in categories.items()}





