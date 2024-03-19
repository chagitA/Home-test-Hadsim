from sqlalchemy import Column, Integer, String, Date
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
    housenum: Mapped[int] = mapped_column()
    birthdate: Mapped[Date] = mapped_column(Date)
    phone: Mapped[str] = mapped_column(String(10))
    cellphone: Mapped[str] = mapped_column(String(10))
