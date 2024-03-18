def RectangularTower():
    height = int(input("Enter tower height:"))
    width = int(input("Enter tower width:"))

    # Calculation of area or perimeter:
    if abs(height - width) > 5 or height == width:
        print("The area of the tower is: ", height * width, " square meter.")
    else:
        print("The perimeter of the tower is: ", 2 * (height + width), " meter.")

