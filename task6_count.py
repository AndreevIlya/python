from itertools import count

start = int(input("Enter start number: "))
for num in count(start):
    if num > start * 2:
        break
    else:
        print(num)