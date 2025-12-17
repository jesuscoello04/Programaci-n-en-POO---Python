class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def moverse(self):
        return f"{self.nombre} se mueve de acuerdo a su especie."

    def comunicacion(self):
        return f"{self.nombre} se comunica mediante sonidos o señales."

    def alimentarse(self):
        return f"{self.nombre} se alimenta con una dieta basada en {self.dieta}."

    def dormir(self):
        return f"{self.nombre} está durmiendo."

    def reproducirse(self):
        return f"{self.nombre} se reproduce según su especie."

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Hábitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamano}")
        print(f"Color: {self.color}")
