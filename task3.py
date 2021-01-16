low_payed_employees = ""
total_salary = 0
count = 0
with open('employees_data.txt') as employees_file:
    for line in employees_file.readlines():
        count += 1
        name, salary = line.split(' ')
        salary = int(salary)
        if salary < 20000:
            if low_payed_employees != "":
                low_payed_employees += ", "
            low_payed_employees += name
        total_salary += salary

print(f"Low payed employees are {low_payed_employees}.")
print(f"Average salary is {total_salary / count}.")