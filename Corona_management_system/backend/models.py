from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Corona_management_system.backend.connect_to_sqlserver import ConnectSQL

Base = ConnectSQL.Base



class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    city = Column(String(30))
    street = Column(String(30))
    house_num = Column(Integer)
    birthdate = Column(Date)
    phone = Column(String(10))
    cellphone = Column(String(10))
    positive_result_date = Column(Date, nullable=True, default=None)
    recovery_date = Column(Date, nullable=True, default=None)
    num_of_vaccines = Column(Integer, default=0)

    image = relationship("Image", uselist=False, back_populates="patient")
    vaccinations = relationship("Vaccination", back_populates="patient")


class Image(Base):
    __tablename__ = 'images'

    image_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    patient = relationship("Patient", back_populates="image")
    data = Column(String())
    image_name = Column(String())
    file_type = Column(String())




class Vaccination(Base):
    __tablename__ = 'vaccinations'

    vaccine_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    date: Mapped[Date] = mapped_column(Date)
    manufacturer: Mapped[str] = mapped_column(String(30))

    patient: Mapped["Patient"] = relationship(back_populates="vaccinations")


Base.metadata.create_all(ConnectSQL.engine)
