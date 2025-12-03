from modelo_animales import Animal

class Ave(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipo_pico):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipo_pico = tipo_pico

    def volar(self):
        return f"{self.nombre} está volando."

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"Tipo de pico: {self.tipo_pico}")
        print("Reino: Ave\n")
