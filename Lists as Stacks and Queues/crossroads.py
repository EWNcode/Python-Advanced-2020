"""
Our favorite super-spy action hero Sam is back from his mission in the previous exam, and he has finally found some time
to go on a holiday. He is taking his wife somewhere nice and they're going to have a really good time, but first, they
have to get there. Even on his holiday trip, Sam is still going to run into some problems and the first one is, of
course, getting to the airport. Right now, he is stuck in a traffic jam at a very active crossroads where a lot of
accidents happen. Your job is to keep track of traffic at the crossroads and report whether a crash happened or everyone
 passed the crossroads safely and our hero is one step closer to a much desired vacation.
The road Sam is on has a single lane where cars queue up until the light goes green. When it does, they start passing
one by one during the green light and the free window before the intersecting road's light goes green. During one second
 only one part of a car (a single character) passes the crossroads. If a car is still in the crossroads when the free
 window ends, it will get hit at the first character that is still in the crossroads.

"""

from collections import deque


def crossroad_solver(green_light_sec, free_window, commands):
    cars = deque()
    index = 0
    counter = 0
    green_light = green_light_sec
    free_time = free_window
    car = []

    while True:
        command = commands[index]
        if command == 'END':
            break
        elif command == 'green':
            for i in range(len(cars)):
                if green_light == 0:
                    break
                current = cars.popleft()
                car = deque(current)
                while True:
                    if not car:
                        break
                    if green_light > 0:
                        car.popleft()
                        green_light -= 1
                    elif free_time > 0:
                        car.popleft()
                        free_time -= 1
                    else:
                        break
                counter += 1
            if car:
                return f'A crash happened!\n{current} was hit at {car[0]}.'
            else:
                green_light = green_light_sec
                free_time = free_window
        else:
            cars.append(command)
        index += 1
    return f'Everyone is safe.\n{counter} total cars passed the crossroads.'


#tests = [
#    [
#        '10',
#        '5',
#        [
#            'Mercedes',
#            'green',
#            'Mercedes',
#            'BMW',
#            'Skoda',
#            'green',
#            'END',
#        ]
#
#    ],
#    [
#            '9',
#            '3',
#            [
#                'Mercedes',
#                'Hummer',
#                'green',
#                'Hummer',
#                'Mercedes',
#                'green',
#                'END',
#            ]
#
#        ],
#
#]
#
#[print(crossroad_solver(int(green_light_sex), int(free_window), commands)) for [green_light, free_window, commands] in tests]

green_light_sec = int(input())
free_window = int(input())

commands = []
while True:
    command = input()
    commands.append(command)
    if command == 'END':
        break

print(crossroad_solver(green_light_sec, free_window, commands))
