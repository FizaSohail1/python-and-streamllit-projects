max_length = 3

def shorten(lst):
    while len(lst) > max_length:
        last_element = lst.pop()
        print(last_element)

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
    shorten(lst)

if __name__ == '__main__':
    main()  