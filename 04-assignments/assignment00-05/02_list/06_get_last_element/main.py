# get last element of the list

def get_last_element(last):
    print(last[-1])

def get_lst():
    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    lst = []
    element = input("Enter an element for list or press enter to stop: ")
    while element != "":
        lst.append(element)
        element = input("Enter an element for list or press enter to stop: ")    

    return lst    

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()  