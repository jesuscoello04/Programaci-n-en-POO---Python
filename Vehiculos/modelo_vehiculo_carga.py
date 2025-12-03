from modelo_vehiculo import Vehiculo

class Vehiculo_Carga(Vehiculo):
    def __init__(self, modelo, color, motor, metodo_arranque, metodo_apagado, climatizacion, tipo_seguridad):
        super().__init__(modelo, color, motor, metodo_arranque, metodo_apagado)
        self.climatizacion = climatizacion
        self.tipo_seguridad = tipo_seguridad

    def activar_volco(self):
        return "El volco se eleva para descargar la carga"
    
    def desactivar_volco(self):
        return "El volco vuelve a su posición normal"
    
    def cargar_material(self, cantidad, tipo):
        return f"Se han cargado {cantidad} kg de {tipo}"
    
    def descargar_material(self):
        return "Se ha iniciado la descarga del material"
    
    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"La climatización del Vehiculo es de forma {self.climatizacion}")
        print(f"La seguridad del Vehiculo es de forma {self.tipo_seguridad}")
        return "Información adquirida exitosamente"