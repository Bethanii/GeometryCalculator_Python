import math

def selection():
    return 3

#method to get cone surface area
def surfaceArea(rad, hi):
    surfaceArea = round(math.pi * rad * (rad + math.sqrt((hi * hi) + (rad**2))), 2)
    return surfaceArea

#method to get cone volume
def volume(rad, hi):
    volume = round((math.pi * rad**2 * (hi/3)), 2)
    return volume

#method to get cone lateral surface area
def latSurfaceArea(rad, hi):
    latSurfaceArea = round(math.pi * rad * slant(rad, hi), 2)
    return latSurfaceArea

#method to get cone slant
def slant(rad, hi):
    slant = round(math.sqrt(rad**2 + hi * hi), 2)
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