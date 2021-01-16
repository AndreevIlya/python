with open("file_task2.txt") as file:
    count = 0
    for line in file.readlines():
        count += 1
        print(f"Line {count} has {len(line.split(' '))} words.")
    print(f"Total {count} lines.")
