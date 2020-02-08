def fix_calendar(numbers):
    swap = False
    for i in range(0, len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            swap = True
    if swap:
        fix_calendar(numbers)
    return numbers


numbers = [3,2,1]
fixed = fix_calendar(numbers)
print(fixed)