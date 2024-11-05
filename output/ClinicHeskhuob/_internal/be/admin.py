from sqlalchemy import create_engine, Column, Integer, NVARCHAR
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class admin(Base):
    __tablename__= "admin"
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR)
    family = Column(NVARCHAR)
    username = Column(NVARCHAR)
    password = Column(NVARCHAR)

    def __init__(self, name="", family="",username="",password=""):
        self.name = name
        self.family = family
        self.username = username
        self.password=password


engine= create_engine("mssql+pyodbc://@./MarkazMoshavereh?driver=ODBC+Driver+17+for+SQL+Server")
Base.metadata.create_all(engine)
