
from modelo_animales import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipo_pelo):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipo_pelo = tipo_pelo

    def amamantar(self):
        return f"{self.nombre} amamanta a sus crías."

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"Tipo de pelo: {self.tipo_pelo}")
        print("Reino: Mamífero\n")
