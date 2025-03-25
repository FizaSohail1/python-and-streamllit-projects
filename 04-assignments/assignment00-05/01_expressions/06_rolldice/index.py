#simulates rolling two dice and print result of each roll as well as total

import random

sides:int = 6

def main():
    dice1: int = random.randint(1,sides)
    dice2: int = random.randint(1,sides)
    result = dice1 + dice2
    print(f"\nDice has {sides} sides each! ")
    print(f"\nDice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"\nTotal of two dice: {result}")

if __name__ == '__main__':
    main()