def RectangularTower():
    height = int(input("Enter tower height:"))
    width = int(input("Enter tower width:"))

    # Calculation of area or perimeter:
    if abs(height - width) > 5 or height == width:
        print("The area of the tower is: ", height * width, " square meter.")
    else:
        print("The perimeter of the tower is: ", 2 * (height + width), " meter.")


def PrintTriangle(height, width):
    middle_groups = (width - 2) // 2
    rows_in_group = (height - 2) // middle_groups
    rest_of_rows = height - 2 - (middle_groups * rows_in_group)
    star_temp = 0
    space_temp = 0

    # Print the first line:
    for i in range(width // 2):
        print(" ", end="")
    print("*")
    star_temp += 1
    space_temp += 1

    # Printing the middle rows:
    for i in range(rows_in_group + rest_of_rows):
        for j in range(width // 2 - 1):
            print(" ", end="")
        for j in range(star_temp + 2):
            print("*", end="")
        print()
    space_temp += 1
    star_temp += 2

    for i in range(middle_groups - 1):
        for x in range(rows_in_group):
            for j in range(width // 2 - space_temp - i):
                print(" ", end="")
            for j in range(i * 2 + 5):
                print("*", end="")
            print()

    # Print the last line:
    for i in range(width):
        print("*", end="")
    print()


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
            PrintTriangle(height, width)


def PrintMainMenu():
    print("-----------------------------")
    print("WELCOME TO TWITTER")
    print("Please select the tower type:")
    print("1. A rectangular tower")
    print("2. A triangular tower")
    print("To log out, please press 3")
    print("-----------------------------")


def main():
    # Menu display:
    global selection
    PrintMainMenu()

    # Choosing a type of tower:
    while True:
        try:
            selection = int(input())

            # Checking the integrity of the input:
            if 0 < selection < 4:
                if selection == 1:
                    RectangularTower()
                    PrintMainMenu()
                elif selection == 2:
                    TriangularTower()
                    PrintMainMenu()
                else:
                    print("Thanks for using Twitter!")
                    break
            else:
                print("The value you entered is invalid. Please enter a number between 1 and 3")
        except ValueError:
            print("The value you entered is invalid. Please enter a number between 1 and 3")


# RectangularTower()

if __name__ == "__main__":
    main()
