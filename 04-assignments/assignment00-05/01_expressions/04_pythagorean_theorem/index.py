import math

def main():
    print("The Pythagon Theorem")

    ab : float = float(input("\nEnter the length of AB: "))
    ac: float = float(input("\nEnter the length AC: "))
    bc:float = math.sqrt(ab **2 + ac **2)
    print(f"\nThe length of side BC (the hypothenuse) is: {bc}")

if __name__ == '__main__':
    main()    