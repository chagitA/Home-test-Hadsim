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
