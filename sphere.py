import math

#setting sphere as selection 1
def selection():
    return 1

def surfaceArea(rad):
    surfaceArea = round((math.pi * 4) * (rad**2), 2)
    return surfaceArea

def volume(rad):
    volume = round((math.pi * 4/3) * (rad**3), 2)
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius: "))

    print("\nThe Surface Area of a Sphere = ", surfaceArea(radius))
    print("The Volume of a Sphere = ", volume(radius), "\n")
    

if __name__ == '__main__':
    prompt()