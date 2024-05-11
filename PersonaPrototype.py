

from Client import Client
from Employee import Employee
from Persona import Persona


class PersonaPrototype:

    def __init__(self):
        self.personas = {}

    def add_persona(self, name, persona: Persona):
        self.personas[name] = persona

    def get_persona(self, name):
        if name in self.personas:
            return self.personas[name].clone()
        else:
            raise ValueError(f"Persona '{name}' not found.")
        

# Create prototype instances
persona_a = Client(Persona(1,"Pacho","Bonito","123","Avenida Miau","321"))
persona_b = Employee(Persona(1,"Limon","Agrio","456","Avenida Frutal","654"))

# Create and populate the Prototype Registry
registry = PersonaPrototype()
registry.add_persona("PersonaA", persona_a)
registry.add_persona("PersonaB", persona_b)

# Clone prototypes from the registry
cloned_prototype_a = registry.get_prototype("PersonaA")
cloned_prototype_b = registry.get_prototype("PersonaB")

# Verify cloned data
print(cloned_prototype_a.data)  # Output: Prototype A Data
print(cloned_prototype_b.data)  # Output: Prototype B Data