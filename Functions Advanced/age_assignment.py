"""
Create a function called age_assignment that receives different amount of names and then different amount of key-value
pairs. The key will be a single letter (first letter of a name), and the value a number (age). For each name, find its
first letter in the key-value pairs and assign the age to the persons name. At the end return a dictionary with all the
names and ages as shown in the example.

"""

def age_assignment(*args, **kwargs):
    dd = {}
    for arg in args:
        dd[arg] = kwargs[arg[0]]
    return dd


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


