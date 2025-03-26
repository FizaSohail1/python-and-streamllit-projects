# copy message

def add_copies(my_list,list_data):
    for i in range(3):
       my_list.append(list_data)

def main():
    message = input("Enter a message you want to copy: ")
    my_list = []
    add_copies(my_list , message)
    print(f"\n {my_list}")

if __name__ == '__main__':
    main()    

