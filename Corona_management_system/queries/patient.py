from sqlalchemy import select

from Corona_management_system.connect_to_sqlserver import ConnectSQL
from Corona_management_system.models import Patient

Base = ConnectSQL.Base
session = ConnectSQL.session


class Patient_queries:
    # A function that sends the newly created patient to the database:
    def new_patient(self, n_id, n_first_name, n_last_name,
                    n_city, n_street, n_house_num,
                    n_birthday, n_phone, n_cellphone,
                    n_positive_result_date, n_recovery_date):

        new_patient = Patient(id=n_id, firstname=n_first_name, lastname=n_last_name,
                              city=n_city, street=n_street, house_num=n_house_num,
                              birthdate=n_birthday, phone=n_phone, cellphone=n_cellphone,
                              positive_result_date=n_positive_result_date, recovery_date=n_recovery_date)
        session.add(new_patient)
        session.commit()

    # A function that sends a patient according to an ID:
    def get_patient(self, patient_id):
        stmt = select(Patient).where(Patient.id == patient_id)
        result = session.execute(stmt)
        for p in result.scalar():
            return p

