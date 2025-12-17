class base_datos_animales:
    def __init__(self):
        self.lista_animales = []
        self.lista_mamiferos = []
        self.lista_reptiles = []
        self.lista_aves = []
        self.lista_insectos = []
        self.lista_peces = []

    def guardar_objeto(self, nuevo_objeto):
        self.lista_animales.append(nuevo_objeto)

    def agregar_varios_objeto(self, lista_nueva):
        self.lista_animales.extend(lista_nueva)

    def imprimir_info(self):
        for objeto in self.lista_animales:
            objeto.imprimir_informacion()