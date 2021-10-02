import math

def selection():
    return 6

def area(baseA, baseB, hi):
    area =  round((baseA + baseB)/2 * hi, 2)
    return area

def median(baseA, baseB):
    median = round(baseA + baseB, 2)
    return median

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF A TRAPEZOID")
    print("----------------------------------------------------------")
    base1 = int(input("Please Enter the base1: "))
    base2 = int(input("Please Enter the base2: "))
    height = int(input("Please Enter the height: "))

    print("\nArea of a Trapezoid = ", area(base1, base2, height))
    print("Median of a Trapezoid = ", median(base1, base2), "\n")

if __name__ == '__main__':
    prompt()