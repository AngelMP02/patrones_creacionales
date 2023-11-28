import tkinter as tk
from tkinter import messagebox
from pizza_deliciosa_builder import PizzaDeliziosoBuilder
from director_pizza import DirectorPizza
from csv_writer import PizzaCSVWriter
from menu_item import  EntradaMenu, Bebida, Postre
from menu import Menu

class InterfazPedidoPizza:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalizar Pizza")

        # Inicializar el menú
        self.menu = self.inicializar_menu()

        self.ingredientes_seleccionados = []
        self.salsa_seleccionada = ""
        self.bebida_seleccionada = ""

        self.create_widgets()

    def create_widgets(self):
        # Botón para personalizar la pizza
        personalizar_button = tk.Button(self.root, text="Personalizar Pizza", command=self.personalizar_pizza)
        personalizar_button.pack(pady=10)

        # Botón para realizar el pedido y guardar en CSV
        pedido_button = tk.Button(self.root, text="Realizar Pedido", command=self.realizar_pedido)
        pedido_button.pack(pady=10)

    def inicializar_menu(self):
        menu = Menu()

        # Agregar elementos al menú
        entrada1 = EntradaMenu("Entrada 1", 5.99, "Descripción de la entrada 1")
        bebida1 = Bebida("Bebida 1", 1.99, "Refresco")
        postre1 = Postre("Postre 1", 3.99, "Chocolate")

        # Agregar la pizza como un elemento del menú
        pizza_builder = PizzaDeliziosoBuilder()
        director = DirectorPizza(pizza_builder)
        director.construir_pizza()
        pizza_personalizada = pizza_builder.get_pizza()

        # Agregar elementos al menú
        menu.agregar_elemento(entrada1)
        menu.agregar_elemento(bebida1)
        menu.agregar_elemento(postre1)
        menu.agregar_elemento(pizza_personalizada)

        return menu

    def personalizar_pizza(self):
        # Abrir una nueva ventana para personalizar la pizza
        ventana_personalizar = tk.Toplevel(self.root)

        # Etiqueta y checkbuttons para ingredientes
        tk.Label(ventana_personalizar, text="Seleccione los ingredientes:").pack(pady=10)

        opciones_ingredientes = ["Tomate", "Mozzarella", "Prosciutto", "Aceitunas", "Champiñones"]
        var_ingredientes = {ingrediente: tk.IntVar() for ingrediente in opciones_ingredientes}

        for ingrediente, var in var_ingredientes.items():
            checkbutton = tk.Checkbutton(ventana_personalizar, text=ingrediente, variable=var)
            checkbutton.pack()

        # Dropdown para seleccionar la bebida
        tk.Label(ventana_personalizar, text="Seleccione la bebida:").pack(pady=10)
        opciones_bebida = ["Coca-Cola", "Pepsi", "Agua", "Jugo"]
        var_bebida = tk.StringVar(ventana_personalizar)
        var_bebida.set(opciones_bebida[0])  # Valor predeterminado

        dropdown_bebida = tk.OptionMenu(ventana_personalizar, var_bebida, *opciones_bebida)
        dropdown_bebida.pack()

        # Agregar botones para añadir/quitar ingredientes y confirmar la selección
        add_button = tk.Button(ventana_personalizar, text="Añadir Ingredientes", command=lambda: self.actualizar_ingredientes(var_ingredientes))
        add_button.pack(pady=5)

        confirmar_button = tk.Button(ventana_personalizar, text="Confirmar", command=lambda: self.confirmar_personalizacion(var_ingredientes, var_bebida, ventana_personalizar))
        confirmar_button.pack(pady=10)

    def actualizar_ingredientes(self, var_ingredientes):
        # Actualizar la lista de ingredientes seleccionados
        self.ingredientes_seleccionados = [ingrediente for ingrediente, var in var_ingredientes.items() if var.get() == 1]

    def confirmar_personalizacion(self, var_ingredientes, var_bebida, ventana_personalizar):
        # Aplicar la personalización a la pizza
        if self.menu.elementos:
            elemento = self.menu.elementos[-1]

            # Verificar si el elemento no es None y tiene el método build
            if elemento is not None and hasattr(elemento, 'build'):
                # Obtener ingredientes seleccionados
                ingredientes_personalizados = [ingrediente for ingrediente, var in var_ingredientes.items() if var.get() == 1]

                # Aplicar la personalización al elemento del menú
                elemento.build(ingredientes_personalizados, var_bebida.get())

                # Cerrar la ventana de personalización
                ventana_personalizar.destroy()
            else:
                messagebox.showwarning("Advertencia", "El elemento del menú no es válido.")
        else:
            messagebox.showwarning("Advertencia", "El menú está vacío.")

    def realizar_pedido(self):
        # Asegúrate de que haya elementos en el menú
        if self.menu.elementos:
            elemento = self.menu.elementos[-1]

            # Verificar si el elemento no es None y tiene el método construir
            if elemento is not None and hasattr(elemento, 'construir'):
                # Construir el elemento utilizando el método construir
                elemento.construir()

                # Mostrar detalles del elemento personalizado
                detalles = (
                    f"Nombre: {elemento.nombre}\n"
                    f"Precio: {elemento.precio}\n"
                    # Agrega detalles específicos del elemento aquí
                )
                messagebox.showinfo("Detalles del elemento personalizado", detalles)

                # Guardar el elemento personalizado en un archivo CSV
                csv_writer = PizzaCSVWriter("elementos_personalizados.csv")
                csv_writer.write_item_to_csv(elemento)
            else:
                messagebox.showwarning("Advertencia", "El elemento del menú no es válido.")
        else:
            messagebox.showwarning("Advertencia", "El menú está vacío.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazPedidoPizza(root)
    root.mainloop()
