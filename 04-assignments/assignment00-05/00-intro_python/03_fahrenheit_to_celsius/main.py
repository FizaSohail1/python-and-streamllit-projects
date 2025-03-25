def main():
    temprature_fahrenhite = input("Enter temperature in Fahrenheit: ")
    temprature_fahrenhite = float(temprature_fahrenhite)
    degree_celsius = (temprature_fahrenhite - 32)*5.0/9.0

    print(f"Temprature: {temprature_fahrenhite}F = {degree_celsius}C")

if __name__ == '__main__':
    main()    