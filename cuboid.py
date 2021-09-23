import math

def surfaceArea():
    pass

def volume(lth, wi, hi):
    volume = lth * wi * hi
    return volume

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A Cuboid")
    print("----------------------------------------------------------")
    length = int(input("Please Enter the length: "))
    width = int(input("Please Enter the width: "))
    height = int(input("Please Enter the height: "))

    print("\nThe Volume of a Cuboid = ", volume(length, width, height))

if __name__ == '__main__':
    prompt()