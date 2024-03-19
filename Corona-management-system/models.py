from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from connect_to_sqlserver import ConnectSQL

Base = ConnectSQL.Base


class Patient(Base):
    __tablename__ = 'patients'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(30))
    street: Mapped[str] = mapped_column(String(30))
    house_num: Mapped[int] = mapped_column()
    birthdate: Mapped[Date] = mapped_column(Date)
    phone: Mapped[str] = mapped_column(String(10))
    cellphone: Mapped[str] = mapped_column(String(10))
    positive_result_date: Mapped[Date] = mapped_column(Date)
    recovery_date: Mapped[Date] = mapped_column(Date)

    vaccinations: Mapped["Vaccination"] = relationship(back_populates="patient")


class Vaccination(Base):
    __tablename__ = 'vaccinations'

    vaccine_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    date: Mapped[Date] = mapped_column(Date)
    manufacturer: Mapped[str] = mapped_column(String(30))

    patient: Mapped["Patient"] = relationship(back_populates="vaccinations")


Base.metadata.create_all(ConnectSQL.engine)
