income = int(input("What's your income? "))
costs = int(input("What are the costs? "))
if income < costs:
    print(f"Your loss is {costs - income}")
elif income == costs:
    print("You have no profit nor loss")
else:
    profit = income - costs
    print(f"Your profit is {profit}")
    print(f"Your profitability is {(profit / costs) * 100: .2f} %")
    employees_count = int(input("How many employees are there: "))
    print(f"Your profit per employee is {profit / employees_count: .2f}")
