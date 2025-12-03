#Clase hija Botella_vidrio

from modelo_botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, marca, capacidad, tapa, diseño, material, tinte):
        super().__init__(marca, capacidad, tapa)
        self.diseño = diseño
        self.material = material
        self.tinte = tinte

    def reutilizar_botella(self):
        print(f"la botella se va a reutilizar. Material:{self.material}")

    def imprimir_info(self):
        super().imprimir_info()
        print(f"El diseño es: {self.diseño}")
        print(f"El material es: {self.material}")
        print(f"El color es: {self.tinte}")
        return "Información Encontrada"
