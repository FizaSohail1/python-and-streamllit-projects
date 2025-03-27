def main():

    min_height:int = 30

    user_height = float(input("What's your height? "))
    if user_height >= min_height:
        print("You're tall enough to ride!")

    else:
        print("You're not tall enough to ride! may be next time!")   

if __name__ == '__main__':
    main()   

