from abc import ABC, abstractmethod

class Planta(ABC):
    def __init__(self, nombre_comun, especie):
        self.nombre_comun = nombre_comun
        self.especie = especie

    @abstractmethod
    def obtener_cuidados(self):
        pass

    def __str__(self):
        return f"{self.especie} ({self.nombre_comun})"

class Flor(Planta):
    def __init__(self, nombre, especie, color):
        super().__init__(nombre, especie)
        self.color = color

    def obtener_cuidados(self):
        return f"Riego regular para mantener el color {self.color}."

class Cactus(Planta):
    def __init__(self, nombre, especie, tiene_espinas):
        super().__init__(nombre, especie)
        self.tiene_espinas = tiene_espinas

    def obtener_cuidados(self):
        return "Riego minimo. Soporta climas secos."
