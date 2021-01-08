def negative_pow(base, exponent):
    """
    Raises base to exponent power. Exponent must be negative by design.
    :param base: float
    :param exponent: int
    :return: float
    """
    if not exponent.lstrip('+-').isdigit():
        print("Exponent is not a number!")
        return
    exponent = int(exponent)
    if exponent >= 0:
        print("We need negative exponent!")
        return
    if exponent is float:
        print("Exponent must be integer!")
        return
    result = 1
    while exponent < 0:
        result *= base
        exponent += 1
    return 1 / result


base = float(input("Enter base: "))
exponent = input("Enter negative exponent: ")
result = negative_pow(base, exponent)
if result is not None:
    print(result)
