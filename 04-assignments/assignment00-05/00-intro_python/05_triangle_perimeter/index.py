bold_italic = "\033[1;3m" #Ansi escape code
reset = "\033[0m"

def main():

 side1 = float(input(f"{bold_italic}Enter first side: {reset}"))
 side2 = float(input(f"{bold_italic}Enter second side: {reset}"))
 side3 = float(input(f"{bold_italic}Enter third side: {reset}"))

 perimeter = side1 + side2 + side3
 print(f"\nThe sum of the three sides of the triangle is: {perimeter}")

if __name__ == '__main__':
 main()
