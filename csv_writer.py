#Contiene la clase PizzaCSVWriter que se encarga de escribir detalles de las pizzas en un archivo CSV.
# csv_writer.py
import csv

class PizzaCSVWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_item_to_csv(self, item):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([item.nombre, item.precio])
