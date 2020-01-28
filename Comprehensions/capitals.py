"""
Using dictionary comprehension write a program that receives countries on the first line separated by comma and space
", " and their corresponding capital cities on the second line (again separated by comma and space ", ") and prints
each country with their capital on a separate line in the format: "{country} -> {capital}"
"""


{print(f'{c} -> {s}') for (c, s) in zip(input().split(','), input().split(', '))}
