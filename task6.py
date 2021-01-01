result = int(input("Enter first day result: "))
desired_result = int(input("Enter desired result: "))
day = 1
increment = 0.1
if result > 0:
    while True:
        print(f"{day} day: {result: .2f} km")
        if result > desired_result:
            break
        day += 1
        result *= 1 + increment

    print(f"Desired result is reached on {day} day - no less than {desired_result} km.")
else:
    print("Desired result will never be reached.")
