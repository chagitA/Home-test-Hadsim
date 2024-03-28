from sqlalchemy import select, func

from Corona_management_system.connect_to_sqlserver import ConnectSQL
from Corona_management_system.models import Vaccination
import patient
Base = ConnectSQL.Base
session = ConnectSQL.session

patient = patient.Patient_queries()
class Vaccination_queries:
    # A function that sends the newly created vaccine to the database:
    def new_vaccine(self, n_patient_id, n_date, n_manufacturer):
        new_vaccine = Vaccination(patient_id=n_patient_id,
                                  date=n_date, manufacturer=n_manufacturer)
        # Updating the current number of vaccination:
        patient.update_num_vaccines(n_patient_id)
        session.add(new_vaccine)
        session.commit()

    # A function that sends a vaccine or a set of vaccines according to an ID:
    def get_vaccine(self, vaccine_id, type_id):
        # Sending a set of vaccines in case of a patient's ID:
        if type(type_id) == "patient_id":
            stmt = select(Vaccination).where(Vaccination.patient_id == vaccine_id)
            result = session.execute(stmt)
            return [v for v in result.scalars()]

        # Sending a single vaccine in case of a vaccine ID:
        else:
            stmt = select(Vaccination).where(Vaccination.vaccine_id == vaccine_id)
            result = session.execute(stmt)
            for v in result.scalar():
                return v

    # A function that checks whether the patient has the maximum possible vaccinations:
    def has_max_vaccines(self, patient_id):
        # Retrieving the number of vaccinations for the client:
        num_vaccinations = (session.query(func.count(Vaccination.vaccine_id))
                            .filter_by(patient_id=patient_id).scalar())
        return num_vaccinations >= 4
