stop = "*"


def increase_by_number(x): return result + x


def sum_input_numbers():
    global result
    while True:
        string = input(f"Enter numbers separated by \" \". Use {stop} to stop: ")
        numbers = string.split(" ")
        stop_flag = False
        for number in numbers:
            if number == stop:
                stop_flag = True
                print("Exiting. Wait for result...")
                break
            if not number.isdigit():
                print(f"Something went wrong, number {number} is leapt.")
                continue
            number = int(number)
            result = increase_by_number(number)

        if stop_flag:
            break


result = 0
sum_input_numbers()
print(f"This is result: {result}")
