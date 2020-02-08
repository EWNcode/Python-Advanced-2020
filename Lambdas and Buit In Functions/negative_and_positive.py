"""
You will receive a list of numbers. Separate the negative numbers from the positive. Find the total sum of the negatives
and positives, replace the negative number with its absolute value and print the following:
If the absolute negative number is bigger than the positive number: 	"The negatives are stronger than the positives"
If the positive number is bigger than the absolute negative number: 	"The positives are stronger than the negatives"

"""

def solve(numbers):
    result = ''
    positive, negative = sum(x for x in numbers if x >= 0), sum(y for y in numbers if y < 0)
    result += str(negative) + '\n'
    result += str(positive) + '\n'
    if positive < abs(negative):
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"

    return result

numbers = sorted(list(map(int, input().split())))
print(solve(numbers))