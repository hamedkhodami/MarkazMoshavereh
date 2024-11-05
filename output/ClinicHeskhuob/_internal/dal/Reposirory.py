from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from be.admin import admin

engine= create_engine("mssql+pyodbc://@./MarkazMoshavereh?driver=ODBC+Driver+17+for+SQL+Server")
Session=sessionmaker(bind=engine)
session=Session()

class Repository():
    def add(self, obj):
            session.add(obj)
            session.commit()


    def read(self, obj):
        return session.query(obj).all()


    def update(self,obj,id,**kwargs):
        objects=self.readbyid(obj,id)
        for key , val in kwargs.items():
            setattr(objects,key,val)
        session.commit()



    def delete(self, obj):
        try:
            session.delete(obj)
            session.commit()
            return True
        except:
            return False



    def readbyid(self, obj, id):
        return session.query(obj).filter(obj.id == id).first()


    def redbyNameConselor(self,obj,name,family,expertise):
        return session.query(obj).filter(obj.name ==name,obj.family==family,obj.expertise==expertise).first()

    def ExistLogin(self,TableName,newobj):
        result=session.query(TableName).filter((TableName.username==newobj.username) & (TableName.password==newobj.password)).all()
        if result==[]:
            return False
        else:
            return True


