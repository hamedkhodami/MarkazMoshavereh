from dal.Reposirory import Repository
from be.visitor import visitor
from be.visitor import conselor

class VisitorService:

    repository=Repository()

    def create_visitor(self,name,family,phone,age,nobat,conselor_id):
            obj=visitor(name=name, family=family, phone=phone, age=age,nobat=nobat, conselor_id=conselor_id)
            self.repository.add(obj)

    def read_visitor(self):
        return self.repository.read(visitor)

    def get_visitor_by_id(self,id):
        return self.repository.readbyid(visitor, id)

    def update_visitor(self,obj,id,**kwargs):
        return self.repository.update(obj,id,**kwargs)


    def delete_visitor(self,id):
        Visitor=self.repository.readbyid(visitor, id)
        if Visitor:
            self.repository.delete(Visitor)

