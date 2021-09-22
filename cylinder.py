# inspiration code for Python Unit Testing Project
import math

def surfaceArea():
    pass

def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return volume

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CYLINDER")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    height = int(input("Please Enter the height :"))

    print("\nThe Volume of a Cylinder = ", volume(radius, height))

if __name__ == '__main__':
    prompt()
