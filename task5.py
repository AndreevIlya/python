with open("numbers.txt", 'w') as numbers_file:
    while True:
        number = input("Enter a number or a blank line to stop: ")
        if number == "":
            break
        numbers_file.write(number + " ")

numbers_sum = 0
with open("numbers.txt") as numbers_file:
    numbers = numbers_file.read()
    print(numbers)
    for number in numbers.split(' '):
        if number.isdigit():
            numbers_sum += int(number)

print(numbers_sum)
