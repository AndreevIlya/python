from random import randrange

numbers = list()
for _ in range(26):
    trial_number = randrange(1, 27)
    if len(numbers) == 0:
        numbers.append(trial_number)
    else:
        success = False
        for i, number in enumerate(numbers):
            if trial_number > number:
                numbers.insert(i, trial_number)
                success = True
                break
        if not success:
            numbers.append(trial_number)
print(*numbers)

numbers = list()
for _ in range(26):
    trial_number = randrange(1, 27)
    numbers.append(trial_number)
print(*sorted(numbers, reverse=True))
