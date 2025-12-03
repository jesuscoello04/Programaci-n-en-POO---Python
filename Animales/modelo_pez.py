from modelo_animales import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipo_agua):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipo_agua = tipo_agua

    def nadar(self):
        return f"{self.nombre} está nadando."

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"Tipo de agua: {self.tipo_agua}")
        print("Reino: Pez\n")
