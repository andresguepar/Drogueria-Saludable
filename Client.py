

import copy



class Client:

    def __init__(self, id = None, name = None, lastName = None, dni = None, addres = None, phone = None):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.dni = dni
        self.addres = addres
        self.phone = phone

    def __str__(self):
        return f"Id Client: {self.id}\nName: {self.name}\n Last Name: {self.lastName}\n" \
               f"DNI: {self.dni}\nAddres: {self.addres}\nPhone: {self.phone}"

    def __copy__(self):
        cls = self.__class__
        new_client = cls.__new__(cls)
        new_client.__dict__.update(self.__dict__)
        return new_client

    def clone(self):
        return copy.copy(self)