def main():
    # Menu display:
    print("Please select the tower type:")
    print("1. A rectangular tower")
    print("2. A triangular tower")
    print("To log out, please press 3")

    # Choosing a type of tower:
    while True:
        try:
            selection = int(input())

            # Checking the integrity of the input:
            if 0 < selection < 4:
                break
            print("The value you entered is invalid. Please enter a number between 1 and 3")
        except ValueError:
            print("The value you entered is invalid. Please enter a number between 1 and 3")


if __name__ == "__main__":
    main()
