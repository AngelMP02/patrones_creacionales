from menu import MenuItem
class Pizza(MenuItem):
    def __init__(self, nombre, precio, tipo_masa, salsa, ingredientes_principales, tecnicas_coccion, presentacion, maridaje_recomendado):
        super().__init__(nombre, precio)
        self.tipo_masa = ""
        self.salsa = ""
        self.ingredientes_principales = []
        self.tecnicas_coccion = ""
        self.presentacion = ""
        self.maridaje_recomendado = ""
        self.bebida = ""  # Agregar el atributo de bebida a la clase Pizza