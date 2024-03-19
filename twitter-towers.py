def RectangularTower():
    height = int(input("Enter tower height:"))
    width = int(input("Enter tower width:"))

    # Calculation of area or perimeter:
    if abs(height - width) > 5 or height == width:
        print("The area of the tower is: ", height * width, " square meter.")
    else:
        print("The perimeter of the tower is: ", 2 * (height + width), " meter.")


def TriangularTower():
    height = int(input("Enter tower height:"))
    width = int(input("Enter tower width:"))

    # Menu display:
    print("Please select an option:")
    print(" - To calculate the perimeter of the triangle, press 1.")
    print(" - To print the triangle, press 2.")

    # Choosing an option:
    while True:
        try:
            option = int(input())

            # Checking the integrity of the input:
            if 0 < option < 3:
                break
            print("The value you entered is invalid. Please enter a number between 1 and 2")
        except ValueError:
            print("The value you entered is invalid. Please enter a number between 1 and 2")

    # Processing the request:
    if option == 1:
        perimeter = 2 * ((height ** 2 + (width / 2) ** 2) ** 0.5) + width
        print("The perimeter of the triangle is ", perimeter, " square meter.")

    else:
        # Checking the conditions for printing the triangle:
        if width % 2 == 0 or width >= 2 * height:
            print("We are sorry, the triangle cannot be printed.")
            return

        else:
            def PrintTriangle():
                print("this function will be activated soon.")

            PrintTriangle()
