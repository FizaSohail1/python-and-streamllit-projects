
C = 299792458 

def main():
    mass = float(input("Enter kilos of mass: "))

    E:float = mass * ( C ** 2)

    print("e * C^2")
    print(f"m = {mass} Kg")
    print(str(E) + " joules of energy!")

if __name__ == '__main__':
    main()   