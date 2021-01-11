from random import randrange

data = [randrange(0, 1000) for _ in range(20)]
print(*data)

saved = max(data) + 1
selected_data = []
for datum in data:
    if datum > saved:
        selected_data.append(datum)
    saved = datum

print(*selected_data)
