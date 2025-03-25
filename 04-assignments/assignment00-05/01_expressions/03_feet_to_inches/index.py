#Fett to inches

INCHES_IN_FOOT: int = 12

def main():
    feet : float = float(input("Number of Feets: "))
    result: float = feet * INCHES_IN_FOOT
    print(F"This is {result} inches!")

if __name__ == "__main__":
    main()    