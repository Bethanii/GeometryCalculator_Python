import math

def surfaceArea():
    pass

def area(baseA, baseB, hi):
    area =  (baseA + baseB)/2 * hi
    return area

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF A TRAPEZOID")
    print("----------------------------------------------------------")
    base1 = int(input("Please Enter the base1 : "))
    base2 = int(input("Please Enter the base2 : "))
    height = int(input("Please Enter the height : "))

    print("\nThe Area of a Trapezoid = ", area(base1, base2, height))

if __name__ == '__main__':
    prompt()