#find the highest number via list

numbers = [21, 33, 44, 12, 10, 99, 1, 103, 23, 31, 88, 47]
highest_number = numbers[0]
for number in numbers:
    if number > highest_number:
        highest_number = number
print(highest_number)
