import random
import time


def display_intro():
    print('''You are in the land of dragons. In front of you, there are
          two caves. In one of them, there is a friendly dragon who 
          is willing to share his treasures with you. In the other, 
          there is a greedy and hungry dragon who will eat you instantly''')


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you enter? (Press 1 or 2)')
        cave = input()
    return cave