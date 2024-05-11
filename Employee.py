import Persona


class Employee(Persona):
       def __init__(self, id = None, name = None, lastName = None, position = None, addres = None, phone = None):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.dni = position
        self.addres = addres
        self.phone = phone