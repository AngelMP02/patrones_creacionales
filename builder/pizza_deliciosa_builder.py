# pizza_deliciosa_builder.py
from pizza_builder import PizzaBuilder
from pizza import Pizza

class PizzaDeliziosoBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = None

    def build_tipo_masa(self):
        # Implementation for building tipo_masa
        pass

    def build_salsa(self):
        # Implementation for building salsa
        pass

    def build_ingredientes_principales(self):
        # Implementation for building ingredientes_principales
        pass

    def build_tecnicas_coccion(self):
        # Implementation for building tecnicas_coccion
        pass

    def build_presentacion(self):
        # Implementation for building presentacion
        pass

    def build_maridaje_recomendado(self):
        # Implementation for building maridaje_recomendado
        pass

    def get_pizza(self):
        return self.pizza

    def build_pizza(self, nombre, precio, tipo_masa, salsa, ingredientes_principales, tecnicas_coccion, presentacion, maridaje_recomendado):
        self.pizza = Pizza(nombre, precio, tipo_masa, salsa, ingredientes_principales, tecnicas_coccion, presentacion, maridaje_recomendado)
