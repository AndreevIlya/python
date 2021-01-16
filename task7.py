import json

firms = {}
average_profit = {}
with open("firm_data.txt") as firm_file:
    total_profit = 0
    count = 0
    for firm in firm_file.readlines():
        name, _, income, costs = firm.split(" ")
        profit = int(income) - int(costs)
        firms[name] = profit
        if profit > 0:
            count += 1
            total_profit += profit
    average_profit["average_profit"] = total_profit / count

data = [firms, average_profit]
with open("firm_data.json", 'w') as firm_json:
    json.dump(data, firm_json)
