def divide_numbers(numerator, denominator):
    try:
        return int(numerator) / int(denominator)
    except ZeroDivisionError:
        print("Denominator is zero! ;(")
    except ValueError:
        print("NAN is input! ;(")


a = input("What to divide: ")
b = input("By what to divide: ")

result = divide_numbers(a, b)
if result is not None:
    print(result)
