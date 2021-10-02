import math

def selection():
    return 2

def surfaceArea(rad, hi):
    surfaceArea = round((2 * math.pi * rad * hi) + 2 * math.pi * rad * rad, 2)
    return surfaceArea

def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return round(volume, 2) 

def latSurfaceArea(rad,hi):
    latSurfaceArea = 2 * math.pi * rad * hi
    return round(latSurfaceArea, 2)

def topOrBottom(rad):
    topOrBottom = math.pi * rad * rad
    return round(topOrBottom, 2)

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CYLINDER")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the radius: "))
    height = int(input("Please Enter the height: "))

    print("\nThe Surface Area of a Cylinder: ", surfaceArea(radius, height))
    print("The Volume of a Cylinder = ", volume(radius, height))
    print("Lateral Surface Area of a Cylinder = ", latSurfaceArea(radius, height))
    print("Top OR Bottom Surface Area of a Cylinder: ", topOrBottom(radius),"\n")

if __name__ == '__main__':
    prompt()
