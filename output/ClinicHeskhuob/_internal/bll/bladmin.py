from dal.Reposirory import Repository
from be.admin import admin

class AdminService:

    repository=Repository()

    def create_admin(self,name,family,username,password):
        obj=admin(name=name, family=family, username=username, password=password)
        self.repository.add(obj)
        return True

    def read_admin(self):
        return self.repository.read(admin)

    def get_admin_by_id(self,id):
        return self.repository.readbyid(admin, id)

    def update_admin(self,obj,id,**kwargs):
        return self.repository.update(obj,id,**kwargs)

    def delete_admin(self,id):
        Admin=self.repository.readbyid(admin, id)
        if Admin:
           return self.repository.delete(Admin)

    def blExistLogin(self,TableName,newobj):
        result=self.repository.ExistLogin(TableName,newobj)
        return result