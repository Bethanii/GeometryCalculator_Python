import math

def surfaceArea(rad, hi):
    surfaceArea = math.pi * rad * (rad + math.sqrt((hi * hi) + (rad * rad)))
    return surfaceArea

def volume(rad, hi):
    volume = (math.pi * rad * rad * (hi/3))
    return volume

def latSurfaceArea(rad,hi):
    latSurfaceArea = math.pi * rad * hi
    return latSurfaceArea

def slant(rad, hi):
    slant = math.sqrt(rad * rad + hi * hi)
    return slant

def prompt():
    print()
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME & SURFACE AREA OF A CONE")
    print("----------------------------------------------------------")
    radius = int(input("Please Enter the Radius of a Cone: "))
    height = int(input("Please Enter the Height of a Cone: "))

    print("\nLength of a Side (Slant) of a Cone = ", slant(radius, height))
    print("The Surface Area of a Cone = ", surfaceArea(radius, height))
    print("The Volume of a Cone = ", volume(radius, height))
    print("The Lateral Surface Area of a Cone = ", latSurfaceArea(radius, height), "\n")

if __name__ == '__main__':
    prompt()