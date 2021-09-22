import math

def surfaceArea():
    pass

def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    height = int(input("Please Enter the height :"))

    print("\nThe Volume of a Sphere = ", volume(radius, height))

if __name__ == '__main__':
    prompt()