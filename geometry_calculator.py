import sphere
#now I can leverage the functions in sphere
#or I could do the "from sphere" to select a function from this class


def main():

    while True:
        print("Welcome to the my Geometry Program")
        print("1. Sphere")
        print("2. Cylinder")
        print("0. Quit")
        selection = int(input("Please enter your selection: "))
        if selection == 0:
            break

main()