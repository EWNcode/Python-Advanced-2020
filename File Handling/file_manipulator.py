
from os import remove


def create_file(file):
    f = open(file, 'w')
    f.close()


def add_to_file(file, content):
    with open(file, 'a') as f:
        f.write(content + '\n')


def replace_on_file(file_name, old, new):

    try:
        with open(file_name, 'r') as file:
            new_file = file.read().replace(old, new)
        with open(file_name, 'w') as file:
            file.write(new_file)

    except:
        print("An error occurred")


def file_delete(file_name):
    try:
        remove(file_name)
    except:
        print("An error occurred")


def file_manipulation():
    while True:
        data = input()
        if data == 'End':
            break
        command, file_name, *args = data.split('-')
        if command == 'Create':
            create_file(file_name)
        elif command == 'Add':
            content = args[0]
            add_to_file(file_name, content)
        elif command == 'Replace':
            old_sting = args[0]
            new_string = args[1]
            replace_on_file(file_name, old_sting, new_string)
        elif command == 'Delete':
            file_delete(file_name)


if __name__ == '__main__':
    file_manipulation()
