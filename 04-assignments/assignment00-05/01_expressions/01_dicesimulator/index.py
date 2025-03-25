import random

sides:int = 6

def roll_dice():
    "Simulates the two dice and prints their total"
    dice1: int = random.randint(1,sides)
    dice2: int = random.randint(1,sides)
    result = dice1 + dice2

    print(f"Total of two dice: {result}")

def main():
    dice1 : int = 10
    print("Die 1 in main() starts as: " + str(dice1))
    roll_dice()
    roll_dice()
    roll_dice()    

    print("Die 1 in main() is: " + str(dice1))

if __name__ == '__main__':
    main()