"""
sing list comprehension, write a program that receives some strings separated by comma and space ", " and prints on the
console each string with its length in the format: "{first_str} -> {first_str_len}, {second_str} -> {second_str_len}…
"""
print(", ".join([f'{name} -> {len(name)}' for name in input().split(', ')]))