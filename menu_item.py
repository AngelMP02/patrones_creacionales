class MenuItem:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
        
class EntradaMenu(MenuItem):
    def __init__(self, nombre, precio, descripcion):
        super().__init__(nombre, precio)
        self.descripcion = descripcion
class Bebida(MenuItem):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo
        
class Postre(MenuItem):
    def __init__(self, nombre, precio, sabor):
        super().__init__(nombre, precio)
        self.sabor = sabor
        
        
