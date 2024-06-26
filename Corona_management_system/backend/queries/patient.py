from sqlalchemy import select

from Corona_management_system.backend.connect_to_sqlserver import ConnectSQL
from Corona_management_system.backend.models import Patient, Image

Base = ConnectSQL.Base
session = ConnectSQL.session


class Patient_queries:
    # A function that sends the newly created patient to the database:
    def new_patient(self, n_id, n_first_name, n_last_name,
                    n_city, n_street, n_house_num,
                    n_birthday, n_phone, n_cellphone):
        new_patient = Patient(id=n_id, firstname=n_first_name, lastname=n_last_name,
                              city=n_city, street=n_street, house_num=n_house_num,
                              birthdate=n_birthday, phone=n_phone, cellphone=n_cellphone)
        session.add(new_patient)
        session.commit()

    # A function that sends the newly created image to the database:
    def new_picture(self, p_id, n_data, n_image_name, n_file_type):
        try:
            new_image = Image(patient_id=p_id, data=n_data, image_name=n_image_name, file_type=n_file_type)
            session.add(new_image)
            session.commit()
        except Exception as e:
            print(e)

    # A function that sends a patient according to an ID:
    def get_patient(self, patient_id):
        stmt = select(Patient).where(Patient.id == patient_id)
        result = session.execute(stmt)
        # for p in result.scalar():
        #     return p
        patient = result.scalar()
        patient_data = {
            'id': patient.id,
            'firstname': patient.firstname,
            'lastname': patient.lastname,
            # Add other attributes as needed
        }
        return patient_data

    def get_image(self, patient_id):
        try:
            # Query the Image table for the image associated with the given patient_id
            image_query = select(Image).filter(Image.patient_id == patient_id)
            result = session.execute(image_query).scalar_one()

            # Return the image data
            return result.data
        except Exception as e:
            print(e)

    # A function that updates the date of receiving a positive result for Corona:
    def update_positive_result_date(self, patient_id, date):
        patient = session.query(Patient).filter(Patient.id == patient_id).one_or_none()

        if patient is not None:
            # Update the positive result date
            patient.positive_result_date = date
            # Commit the changes to the database
            session.commit()

    # A function that updates the date of recovery from Corona:
    def update_recovery_date(self, patient_id, date):
        patient = session.query(Patient).filter(Patient.id == patient_id).one_or_none()

        if patient is not None:
            # Update the recovery result date
            patient.recovery_date = date
            # Commit the changes to the database
            session.commit()

    def update_num_vaccines(self, patient_id):
        patient = session.query(Patient).filter(Patient.id == patient_id).one_or_none()
        num_of_vaccine = session.query(Patient.num_of_vaccines).filter(Patient.id == patient_id).one_or_none()
        if num_of_vaccine <= 4:
            patient.num_of_vaccines += 1
            session.commit()

