#International voting age

PETURKSBOUIPO_AGE: int = 16
MAYENGUA_AGE: int = 48
STANLAU: int = 25

def main():

    user_input = int(input("How old are you? "))

    if user_input >= PETURKSBOUIPO_AGE:
        print("\nYou can vote in peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE))
    else:
        print("You cannot vote in peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE))

    if user_input >= MAYENGUA_AGE:
        print("\nYou can vote in MAYENGUA_AGE where the voting age is " + str(MAYENGUA_AGE))
    else:
        print("You cannot vote in MAYENGUA_AGE where the voting age is " + str(MAYENGUA_AGE))
    if user_input >= STANLAU:
        print("\nYou can vote in STANLAU where the voting age is " + str(STANLAU))
    else:
        print("You cannot vote in STANLAU where the voting age is " + str(STANLAU))
      
       
if __name__ == '__main__':
    main()