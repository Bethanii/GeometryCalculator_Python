import math

def surfaceArea():
    pass

def area(lth):
    area =  (math.sqrt(3)/4) * lth * lth
    return area

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF AN EQUILATERAL TRIANGLE")
    print("----------------------------------------------------------")
    length = int(input("Please Enter Length of any side of an Equilateral Triangle : "))

    print("\nArea of a Equilateral Triangle = ", area(length))

if __name__ == '__main__':
    prompt()
