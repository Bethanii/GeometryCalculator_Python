import sphere, cylinder, cone, cube, triangle, trapezoid, cuboid, equilateralTriangle
from flask import Flask

def main():

    while True:
        #Main menu output
        print("Welcome to the my Geometry Program")
        print("1. Sphere")
        print("2. Cylinder")
        print("3. Cone")
        print("4. Triangle")
        print("5. Cube")
        print("6. Trapezoid")
        print("7. Cuboid")
        print("8. Equilateral Triangle")
        print("0. Quit")

        #Get user selection from menu
        selection = int(input("Please enter your selection: "))

        #call appropriate method
        if selection == 0:
            break
        if selection == 1:
            sphere.prompt()
            break
        if selection == 2: 
            cylinder.prompt()
            break
        if selection == 3: 
            cone.prompt()
            break
        if selection == 4: 
            cube.prompt()
            break
        if selection == 5: 
            triangle.prompt()
            break
        if selection == 6: 
            trapezoid.prompt()
            break
        if selection == 7: 
            cuboid.prompt()
            break
        if selection == 8: 
            equilateralTriangle.prompt()
            break

main()