import math

def selection():
    return 5

def perimeter(sideA, sideB, sideC):
    perimeter = round(sideA + sideB + sideC, 2)
    return perimeter

def semiPerimeter(sideA, sideB, sideC):
    semiPerimeter = round((sideA + sideB + sideC)/2, 2)
    return semiPerimeter

def area(sideA, sideB, sideC):
    sp = semiPerimeter(sideA, sideB, sideC)
    area = round(math.sqrt(sp * (sp - sideA) * (sp - sideB) * (sp - sideC)), 2)
    return area

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA OF A TRIANGLE")
    print("----------------------------------------------------------")
    side1 = int(input("Please Enter the First side of a Triangle: "))
    side2 = int(input("Please Enter the Second side of a Triangle: "))
    side3 = int(input("Please Enter the Third side of a Triangle: "))

    print("\nThe Perimeter of a Triangle = ", perimeter(side1, side2, side3))
    print("The Semi Perimeter of a Triangle = ", semiPerimeter(side1, side2, side3))
    print("The Area of a Triangle = ", area(side1, side2, side3), "\n")

if __name__ == '__main__':
    prompt()
