from modelo_animales import Animal

class Reptil(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipo_escamas):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipo_escamas = tipo_escamas

    def regular_temperatura(self):
        return f"{self.nombre} regula su temperatura tomando sol."

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"Tipo de escamas: {self.tipo_escamas}")
        print("Reino: Reptil\n")
