from pizza import MenuItem

class Menu:
    def __init__(self, elementos=None):
        if elementos is None:
            elementos = []
        self.elementos = elementos

    def agregar_elemento(self, elemento):
        if isinstance(elemento, MenuItem):
            self.elementos.append(elemento)
        else:
            print(f"Advertencia: No se pudo agregar el elemento al menú. El elemento debe ser una instancia de MenuItem.")
