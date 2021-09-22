#change formula
import math

def surfaceArea():
    pass

def volume(side):
    volume = side * side * side
    return volume

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CUBE")
    print("----------------------------------------------------------")
    sideLength = int(input("Please Enter the Length of any Side of a Cube:"))

    print("\nThe Volume of a Cube = ", volume(sideLength))

if __name__ == '__main__':
    prompt()