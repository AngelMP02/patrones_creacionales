class ElementoMenu:
    def __init__(self, nombre, codigo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio

    def obtener_precio(self):
        return self.precio