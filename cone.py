import math

def surfaceArea():
    pass

def volume(rad, hi):
    volume = (math.pi * rad * rad * hi)/3
    return volume

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CONE")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the Radius of a Cone:"))
    height = int(input("Please Enter the Height of a Cone :"))

    print("\nThe Volume of a Cone = ", volume(radius, height))

if __name__ == '__main__':
    prompt()