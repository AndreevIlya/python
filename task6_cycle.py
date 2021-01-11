from itertools import cycle
from time import sleep

string = input("Say something: ")
countdown = 5 * len(string)
for letter in cycle(string):
    if countdown == 0:
        break
    print(letter, end='')
    sleep(0.2)
    countdown -= 1
    if countdown % len(string) == 0:
        print()
