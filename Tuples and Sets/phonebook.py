"""
Write a program that receives some info from the console about people and their phone numbers. You are free to choose
the way the data is entered; each entry should have just one name and one number (both strings). If you receive a name
that already exists in the phonebook, simply update its number. After filling this simple phonebook, upon receiving
the command "search", your program should be able to perform a search of a contact by name and print her details in
format "{name} -> {number}". In case the contact isn't found, print "Contact {name} does not exist."
"""

from collections import deque

def read_until_command(end_command):
    commands = []
    while True:
        command = input()
        if end_command == command:
            return commands
        commands.append(command)


def phonebook_solve():
    phone_book = deque(read_until_command('search'))
    searched = deque(read_until_command('stop'))
    phone_dict = {}
    result = ''

    while len(phone_book) > 0:
        command = phone_book.popleft()
        name, phone = command.split('-')
        phone_dict[name] = phone

    while len(searched) > 0:
        s = searched.popleft()
        if s in phone_dict.keys():
            result += ''.join(
                [''.join('{} -> {}'.format(k, v)) for k, v in phone_dict.items() if k == s]) + '\n'
        else:
            result += f'Contact {s} does not exist.\n'


    return result

print(phonebook_solve())

#tests = [
#    [
#        'Adam-0888080808',
#        'search',
#        'Mery',
#        'Adam',
#        'stop',
#    ],
#    [
#        'Adam-+359888001122',
#        'Ralf-666',
#        'George-5559393',
#        'Silvester-02/987665544',
#        'search',
#        'Silvester',
#        'silvester',
#        'Rolf',
#        'Ralf',
#        'stop'
#    ]
#]
#
#[print(phonebook_solve(commands)) for commands in tests]

#test = []
#while True:
#    test.append(input())
#    if test[-1] == 'stop':
#        print(phonebook_solve(test))
#        break
#

print(phonebook_solve())