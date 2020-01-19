"""
Our favorite super-spy action hero Sam is back from his mission in another exam, and this time he has an even more
difficult task. He needs to unlock a safe. The problem is that the safe is locked by several locks in a row, which
all have varying sizes. Our hero posesses a special weapon though, called the Key Revolver, with special bullets.
Each bullet can unlock a lock with a size equal to or larger than the size of the bullet. The bullet goes into the
keyhole, then explodes, completely destroying it. Sam doesn't know the size of the locks, so he needs to just shoot
at all of them, until the safe runs out of locks. What's behind the safe, you ask? Well, intelligence! It is told
that Sam's sworn enemy – Nikoladze, keeps his top secret Georgian Chacha Brandy recipe inside. It's valued differently
across different times of the year, so Sam's boss will tell him what it's worth over the radio. One last thing, every
bullet Sam fires will also cost him money, which will be deducted from his pay from the price of the intelligence.
Good luck, operative.

"""

from collections import deque

def key_solver(bullet_price, gun_size, bullets, locks, value_of_recepie):
    total_price = 0
    locks = deque(locks)
    result = ''
    counter = 0

    while bullets:
        if counter == gun_size:
            result += 'Reloading!\n'
            counter = 0
        try:
            lock = int(locks.popleft())
        except:
            break
        bullet = int(bullets.pop())
        total_price += bullet_price
        counter += 1
        if not bullet <= lock:
            result += 'Ping!\n'
            locks.appendleft(lock)
        else:
            result += 'Bang!\n'
    if locks:
        result += f'Couldn\'t get through. Locks left: {len(locks)}'
    else:
        money_earned = value_of_recepie - total_price
        result += f'{len(bullets)} bullets left. Earned ${money_earned}'
    return result


tests = [
    [
        '50',
        '2',
        '11 10 5 11 10 20',
        '15 13 16',
        '1500',
    ],
    [
        '20',
        '6',
        '14 13 12 11 10 5',
        '13 3 11 10',
        '800',
    ],
    [
        '33',
        '1',
        '12 11 10',
        '10 20 30',
        '100',
    ]
]

[print(key_solver(int(a), int(b), c.split(), d.split(), int(e))) for [a, b, c, d, e] in tests]

