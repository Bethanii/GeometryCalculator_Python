#change formula
import math

def selection():
    return 4

def surfaceArea(side):
    surfaceArea = round(6 * side * side, 2)
    return surfaceArea

def volume(side):
    volume = round(side * side * side, 2)
    return volume

def latSurfaceArea(side):
    latSurfaceArea = round(4 * side * side, 2)
    return latSurfaceArea 

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CUBE")
    print("----------------------------------------------------------")
    sideLength = int(input("Please Enter the Length of any Side of a Cube: "))
    
    print("\nSurface Area of cube = ", surfaceArea(sideLength))
    print("The Volume of a Cube = ", volume(sideLength))
    print("Lateral Surface of Cube = ", latSurfaceArea(sideLength), "\n")

if __name__ == '__main__':
    prompt()