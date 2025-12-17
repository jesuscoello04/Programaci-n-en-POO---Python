class base_datos_vehiculos:
    def __init__(self):
        self.lista_vehiculos = []
        self.lista_deportivos = []
        self.lista_transporte = []
        self.lista_carga = []

    def guardar_objeto(self, nuevo_objeto):
        self.lista_vehiculos.append(nuevo_objeto)

    def agregar_varios_objeto(self, lista_nueva):
        self.lista_vehiculos.extend(lista_nueva)

    def imprimir_info(self):
        for objeto in self.lista_vehiculos:
            objeto.imprimir_informacion()