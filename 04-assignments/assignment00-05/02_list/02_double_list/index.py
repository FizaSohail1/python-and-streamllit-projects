# Double list

def main():
    num_list:list[int] = [1,2,3,4,5]
    #List comperihension [new_item for item in itereble]
    double = [num * 2 for num in num_list]
    print("\nThis program prints the double of each element in list")
    return print("\n",double)

if __name__ == '__main__':
    main()
   
