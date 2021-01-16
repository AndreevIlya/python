with open('file1.txt', 'w') as file:
    while True:
        string = input("Enter something or empty line to stop: ")
        if string == '':
            break
        file.write(string)
