from dal.Reposirory import Repository
from be.visitor import conselor

class ConselorService:

    repository=Repository()

    def create_conselor(self,name,family,phone,expertise):
        obj=conselor(name=name, family=family, phone=phone, expertise=expertise)
        self.repository.add(obj)
        return True

    def read_conselor(self):
        return self.repository.read(conselor)

    def get_conselor_by_id(self,id):
        return self.repository.readbyid(conselor, id)

    def get_Conselor_by_Name(self,name,family,expertise):
        return self.repository.redbyNameConselor(conselor, name, family, expertise)

    def update_conselor(self,obj,id,**kwargs):
        return self.repository.update(obj,id,**kwargs)


    def delete_conselor(self,id):
        Conselor=self.repository.readbyid(conselor, id)
        if Conselor:
            return self.repository.delete(Conselor)


