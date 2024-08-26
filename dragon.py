import random
import time


def display_intro():
    print('''You are in the land of dragons. In front of you, there are
two caves. In one of them, there is a friendly dragon who 
is willing to share his treasures with you. In the other, 
there is a greedy and hungry dragon who will eat you instantly''')
    print()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you enter? (Press 1 or 2)')
        cave = input()
    return cave


def check_cave(chosen_cave):
    print("you approach the cave...")
    time.sleep(3)
    print("it's dark and spooky...")
    time.sleep(3)
    print("a large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(3)
    print()

    friendly_cave = str(random.randint(1, 2))

    if chosen_cave == friendly_cave:
        print("gives you his treasure!")
    else:
        print("gobbles you down in one bite!")


play_again = "yes"
while play_again == "yes" or play_again == "y":
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    print("do you want to play again? (yes or no)")
    play_again = input()
