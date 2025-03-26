#mad libs


def main():
    adjective:str = str(input("Enter an adjective: "))
    verb :str = str(input("Enter a verb: "))
    noun:str = str(input("Enter a noun: "))

    SENTENCE = f'The {adjective} cat loves to {verb} in the {noun}!'

    print("\n",SENTENCE)

if __name__ == '__main__':
    main()    
    