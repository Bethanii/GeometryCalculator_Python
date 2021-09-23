import math

def surfaceArea(rad):
    surfaceArea = (math.pi * 4) * rad * rad
    return surfaceArea

def volume(rad):
    volume = (math.pi * 4/3) * (rad * rad * rad)
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius: "))

    print("\nThe Volume of a Sphere = ", volume(radius))
    print("The Surface Area of a Sphere = ", surfaceArea(radius), "\n")

if __name__ == '__main__':
    prompt()