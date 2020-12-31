number = int(input("Give me a number: "))
biggest_digit = 0
while True:
    residue = number // 10
    last_digit = number % 10
    if biggest_digit < last_digit:
        biggest_digit = last_digit
    if residue == 0 or biggest_digit == 9:
        print(f"Max digit is {biggest_digit}")
        break
    number = residue
