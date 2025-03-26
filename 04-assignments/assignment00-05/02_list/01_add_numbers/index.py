def add_numbers(num_list):

    total : int =0 

    for number in num_list:
        total += number

    return total

def main():
    numbers:list[int] = [1,2,3,4,5]
    sum_of_nums = add_numbers(numbers)

    print(sum_of_nums)

if __name__ == '__main__':
    main()    
