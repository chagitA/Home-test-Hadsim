from Corona_management_system.backend.connect_to_sqlserver import ConnectSQL
from Corona_management_system.backend.models import Patient
from datetime import datetime, timedelta

Base = ConnectSQL.Base
session = ConnectSQL.session


def active_patients_last_month():
    # Initialize a dictionary to store counts for each day
    active_patients_count = {}

    # Get the current date and time
    end_date = datetime.now()

    # Calculate the start date (30 days ago)
    start_date = end_date - timedelta(days=30)

    # Iterate over each day within the last month
    current_date = start_date
    while current_date <= end_date:
        # Query the database for active patients on the current day
        active_patients = session.query(Patient).filter(
            Patient.positive_result_date <= current_date,
            (Patient.recovery_date == None) | (Patient.recovery_date > current_date)
        ).count()

        # Store the count for the current day
        active_patients_count[current_date.strftime('%Y-%m-%d')] = active_patients

        # Move to the next day
        current_date += timedelta(days=1)

    return active_patients_count


def get_non_vaccinated_patients_count():
    # Query patients who are positive for COVID-19 and not vaccinated
    non_vaccinated_positive_patients = session.query(Patient).filter(
        Patient.num_of_vaccines == 0
    ).count()

    return non_vaccinated_positive_patients
