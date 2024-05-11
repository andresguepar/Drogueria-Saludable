from Client import Client


class ClientPrototype:

    def __init__(self, prototype_client):
        self.prototype_client = prototype_client

    def clone_client(self, idProducto, dni=None):
        new_client = self.prototype_client.clone()
        new_client.idProducto = idProducto
        if dni is not None:
            new_client.dni = dni
        return new_client
    

