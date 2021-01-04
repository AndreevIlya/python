goods = list()
for i in range(5):
    name = input("Enter good's name: ")
    price = input("Enter good's price: ")
    count = input("Enter good's count: ")
    dimen = input("Enter good's dimension: ")
    good = {"name": name, "price": price, "count": count, "dimen": dimen}
    goods.append((i, good))
    print()

for good in goods:
    print(f"{good[0] + 1} {good[1].get('name')} ${good[1].get('price')} {good[1].get('count')} {good[1].get('dimen')}\n")

analytics = dict()
for info in ["name", "price", "count", "dimen"]:
    data = list()
    for good in goods:
        data.append(good[1].get(info))
    analytics[info] = data

for info, data in analytics.items():
    data_string = ""
    for datum in data:
        data_string += datum + " "
    print(f"{info}: {data_string}")
