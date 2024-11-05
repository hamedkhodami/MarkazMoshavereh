from sqlalchemy import create_engine, Column, NCHAR, Integer, NVARCHAR,ForeignKey
from sqlalchemy.orm import declarative_base,relationship



Base = declarative_base()


class visitor(Base):
    __tablename__= "visitor"
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR)
    family = Column(NVARCHAR)
    phone = Column(NCHAR(15))
    age = Column(Integer)
    nobat=Column(NVARCHAR)
    conselor_id = Column(Integer,ForeignKey("conselor.id"))

    conselor = relationship("conselor", back_populates="visitor")


    def __init__(self, name="", family="",phone=0,age=0,nobat="",conselor_id=0):
        self.name = name
        self.family = family
        self.phone = phone
        self.age=age
        self.nobat=nobat
        self.conselor_id=conselor_id

class conselor(Base):
    __tablename__= "conselor"
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR)
    family = Column(NVARCHAR)
    phone = Column(NCHAR(15))
    expertise=Column(NVARCHAR)

    visitor = relationship("visitor", back_populates="conselor")




    def __init__(self, name="", family="", phone=0,expertise=""):
        self.name = name
        self.family = family
        self.phone = phone
        self.expertise=expertise



engine= create_engine("mssql+pyodbc://@./MarkazMoshavereh?driver=ODBC+Driver+17+for+SQL+Server")
Base.metadata.create_all(engine)