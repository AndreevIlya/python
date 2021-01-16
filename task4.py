translation = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
with open('english_numbers.txt') as english_file, open('russian_numbers.txt', 'w', encoding='utf8') as russian_file:
    for line in english_file.readlines():
        word, number = line.split(' - ')
        russian_file.write(f"{translation.get(word.lower()).title()} - {number}")
