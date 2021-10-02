import math

def selection():
    return 7

def surfaceArea(lth, wi, hi):
    surfaceArea = round((2 * lth * wi) + (2 * lth * hi) + (2 * hi * wi), 2)
    return surfaceArea

def volume(lth, wi, hi):
    volume = round(lth * wi * hi, 2)
    return volume

def latSurfaceArea(lth, wi, hi):
    latSurfaceArea = round(2 * hi * (lth + wi), 2)
    return latSurfaceArea

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A Cuboid")
    print("----------------------------------------------------------")
    length = int(input("Please Enter the length: "))
    width = int(input("Please Enter the width: "))
    height = int(input("Please Enter the height: "))

    print("\nThe Surface Area of a Cuboid = ", surfaceArea(length, width, height))
    print("he Volume of a Cuboid = ", volume(length, width, height))
    print("The Lateral Surface Area of a Cuboid = ", latSurfaceArea(length, width, height), "\n")

if __name__ == '__main__':
    prompt()