import sphere, cylinder, triangle, cone, cube
#now I can leverage the functions in sphere
#or I could do the "from sphere" to select a function from this class


def main():

    while True:
        print("Welcome to the my Geometry Program")
        print("1. Sphere")
        print("2. Cylinder")
        print("3. Cone")
        print("4. Triangle")
        print("5. Cube")
        print("0. Quit")
        selection = int(input("Please enter your selection: "))
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
            triangle.prompt()
            break
        if selection == 5: 
            cube.prompt()
            break

main()