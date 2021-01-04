text = input("Enter text: ")
words = text.split(" ")
for i, word in enumerate(words):
    print(f"{i + 1} {word[:10]}")
