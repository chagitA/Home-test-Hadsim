from datetime import datetime


# Function for checking a valid Israeli ID number:
def israeli_id_validation(id_number):
    # Ensure the ID number is composed of exactly nine digits
    if not (id_number.isdigit() and len(id_number) == 9):
        return False

    # Calculate the sum of the digits according to the ID validation algorithm
    sum_ = sum(int(digit) * (1 if i % 2 == 0 else 2) % 10 + int(digit) * (1 if i % 2 == 0 else 2) // 10
               for i, digit in enumerate(id_number))
    # Check if the sum is divisible by 10
    return sum_ % 10 == 0


# Function to verify correct date for recovery:
def validation_recovery_date(ill_date, reco_date):
    # Convert string dates to datetime objects
    ill_date = datetime.strptime(ill_date, "%Y-%m-%d")
    reco_date = datetime.strptime(reco_date, "%Y-%m-%d")

    # Check if recovery date is after illness date and not on the same day
    if reco_date > ill_date and reco_date.date() != ill_date.date():
        return True
    else:
        return False


# A function that verifies a phone number:
def verify_phone_number(phone_number):
    # Check if the string contains only digits
    if not phone_number.isdigit():
        return False

    # Check if the length of the number is 9 or 10 digits and starts with 0
    if len(phone_number) == 9 or len(phone_number) == 10:
        if phone_number[0] == '0':
            return True

    return False


# A function that verifies a cellphone number:
def verify_cellphone_number(phone_number):
    # Check if the string contains only digits and has length 10
    if phone_number.isdigit() and len(phone_number) == 10:
        # Check if the number starts with "05"
        if phone_number.startswith("05"):
            return True

    return False
