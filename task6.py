# PyCharm recommends not to assign lambda but to use def O_O
capitalize_word = lambda string: string.title()

string = input("Enter a sentence: ")
for word in string.split(" "):
    print(f"{capitalize_word(word)} ", end="")