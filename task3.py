months_dict = {"winter": (12, 1, 2), "spring": (3, 4, 5,), "summer": (6, 7, 8), "autumn": (9, 10, 11)}
months_list = ["winter", "spring", "summer", "autumn"]

month = None
while True:
    month = input("Enter month number (from 1): ")
    if month.isdigit():
        month = int(month)
        if 0 < month < 13:
            break
    print("Try again.")

for season in months_dict:
    if month in months_dict[season]:
        print(f"Season from dict is {season}")

if month == 12:
    print(f"Season from list is {months_list[0]}")
else:
    print(f"Season from list is {months_list[month // 3]}")
