# get last element of the list


def main():
    my_list = []
    element = input("Enter an element for list or press enter to stop: ")
    while element != "":
        my_list.append(element)
        element = input("Enter an element for list or press enter to stop: ")    

    return print("Here is the List: ",my_list)   

if __name__ == '__main__':
    main()  