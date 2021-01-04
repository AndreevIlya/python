items = list()
count = int(input("Enter list's length: "))
print("Enter items:")
for i in range(count):
    items.append(input())
transformed_items = list()
for i in range(0, count, 2):
    if i != len(items) - 1:
        transformed_items.append(items[i + 1])
    transformed_items.append(items[i])
print(transformed_items)
