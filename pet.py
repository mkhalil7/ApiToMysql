# Class defintion for the pet
class pet:
    def __init__(self, id, name, photoUrls, status):
        self.name = name
        self.id = id
        self.photoUrls = photoUrls
        self.status = status


    def set_name(self,name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_photoUrls(self, photoUrls):
        self.photoUrls = photoUrls

    def set_status(self,status):
        self.status = status

    def get_name(self):
        return self.name

    def get_id(self, id):
        return id

    def get_photoUrls(self):
        return self.photoUrls

    def get_status(self):
        return self.status



