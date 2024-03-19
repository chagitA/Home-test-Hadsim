import sqlalchemy as db
import urllib
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker, declarative_base


class ConnectSQL:
    DRIVER_NAME = "ODBC Driver 17 for SQL Server"
    SERVER_NAME = "DESKTOP-E20A7OU\SQLEXPRESS"
    DATABASE_NAME = "HMODatabase"

    quoted = urllib.parse.quote_plus(f"DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes")
    engine = db.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    conn = engine.connect()

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    def __init__(self):
        pass
