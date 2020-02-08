from collections import deque

n_of_materials = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))

dd = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
while len(magic_values) > 0 and len(n_of_materials) > 0:
    material_value = n_of_materials.pop()
    magic_value = magic_values.popleft()
    result = material_value * magic_value
    if result == 0:
        if magic_value == 0 and material_value > 0:
            n_of_materials.append(material_value)
        elif magic_value > 0 and material_value == 0:
            magic_values.appendleft(magic_value)
    elif result < 0:
        result = material_value + magic_value
        n_of_materials.append(result)
    elif result == 400:
        dd['Bicycle'] += 1
    elif result == 300:
        dd['Teddy bear'] += 1
    elif result == 250:
        dd['Wooden train'] += 1
    elif result == 150:
        dd['Doll'] += 1
    elif result > 0:
        result = material_value + 15
        n_of_materials.append(result)

bear_bicycle = 0
doll_train = 0

for k,v in dd.items():
    if k == 'Doll' or k == 'Wooden train':
        if v > 0:
            bear_bicycle += 1
    elif k == 'Teddy bear' or k == 'Bicycle':
        if v > 0:
            doll_train += 1
if bear_bicycle > 1 or doll_train > 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

n_of_materials = list(map(str, n_of_materials))
magic_values = list(map(str, magic_values))

if len(n_of_materials) > 0:
    print(f'Materials left: {", ".join(list(reversed(n_of_materials)))}')
if len(magic_values) > 0:
    print(f'Magic left: {", ".join(list(magic_values))}')

for key, value in sorted(dd.items()):
    if not value == 0:
        print(f'{key}: {value}')