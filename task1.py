from sys import argv

_, hours, salary_per_hour, bonus = argv

print(f"Your earned {int(hours) * int(salary_per_hour) + int(bonus)} $!")
