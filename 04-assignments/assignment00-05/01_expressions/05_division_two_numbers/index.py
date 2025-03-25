def main():
    num1: int = int(input("Enter an integer to be divided: "))
    num2:int = int(input("Enter an integer to divided by: "))

    division:int = num1 // num2
    reminder: int = num1 % num2

    print("\nThe result of this division is "+ str(division) + " with the reminder "+ str(reminder))

if __name__ == '__main__':
    main()    
