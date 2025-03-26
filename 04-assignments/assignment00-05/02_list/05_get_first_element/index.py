# prints the first element of list
def get_First_element(lst):
    print(lst[0])

def get_lst():
    lst = []
    element = input("Enter an element for list or press enter to stop: ")
    while element != "":
        lst.append(element)
        element = input("Enter an element for list or press enter to stop: ")    

    return lst

def main():
    lst = get_lst()
    get_First_element(lst)

if __name__ == '__main__':
    main()        