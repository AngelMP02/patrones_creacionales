# composite.py
from abc import ABC, abstractmethod

class ComponenteMenu(ABC):
    @abstractmethod
    def calcular_precio(self):
        pass
