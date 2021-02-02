class NaNInterruptionException(Exception):
    def __str__(self):
        return "NaN is input!"


list_of_numbers = []


def fill_list():
    datum = input("Enter something or \"stop\" to stop: ")
    if datum == "stop":
        return True
    if not datum.isdigit():
        raise NaNInterruptionException()
    list_of_numbers.append(int(datum))
    return False


while True:
    try:
        if fill_list():
            break
    except NaNInterruptionException as exc:
        print(exc)

print(*list_of_numbers)
