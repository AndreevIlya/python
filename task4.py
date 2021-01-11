from random import randrange

data = [randrange(0, 20) for _ in range(20)]
print(*data)


def check_x_count_1(x):
    global data
    count = 0
    for datum in data:
        if datum == x:
            count += 1
        if count > 1:
            return False
    return True


chosen_data = [x for x in data if check_x_count_1(x)]
print(*chosen_data)
