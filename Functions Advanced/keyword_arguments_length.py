"""
Create a function called kwargs_length which can receive different amount of keyword arguments and returns their length.

"""


def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))