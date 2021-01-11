def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial


n = int(input("Enter n: "))
for el in fact(n):
    print(el)
