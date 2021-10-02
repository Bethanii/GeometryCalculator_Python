import math

def selection():
    return 8

def area(lth):
    area =  round((math.sqrt(3)/4) * lth * lth, 2)
    return area

def perimeter(lth):
    perimeter = round(3 * lth, 2)
    return perimeter

def semiPerimeter(lth):
    semiPerimeter = round((3 * lth)/2, 2)
    return semiPerimeter

def altitude(lth):
    altitude = round((1/2) * math.sqrt(3) * lth, 2)
    return altitude

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF AN EQUILATERAL TRIANGLE")
    print("----------------------------------------------------------")
    length = int(input("Please Enter Length of any side of an Equilateral Triangle: "))

    print("\nArea of a Equilateral Triangle = ", area(length))
    print("Perimeter of a Equilateral Triangle = ", perimeter(length))
    print("Semi Perimeter of a Equilateral Triangle = ", semiPerimeter(length))
    print("Altitude of a Equilateral Triangle = ", altitude(length),"\n")

if __name__ == '__main__':
    prompt()
