random_list = [1, "2", None, [1, "two"], ("three", "four")]
for el in random_list:
    print(type(el))
    if type(el) is list:
        print("list is found")
