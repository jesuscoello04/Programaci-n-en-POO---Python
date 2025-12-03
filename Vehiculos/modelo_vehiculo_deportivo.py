from modelo_vehiculo import Vehiculo

class Vehiculo_Deportivo(Vehiculo):
    def __init__(self, modelo, motor,color, metodo_arranque, metodo_apagado,climatizacion, tipo_seguridad):
        super().__init__(modelo, color, motor, metodo_arranque, metodo_apagado)
        self.climatizacion = climatizacion
        self.tipo_seguridad = tipo_seguridad
        
    def activar_modo_sport(self):
        return "El modo sport se ha activado. La respuesta del motor aumenta."

    def abrir_capota(self):
        return "La capota del deportivo se abre automáticamente."

    def cerrar_capota(self):
        return "La capota del deportivo se cierra."
    
    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"La climatización del Vehiculo es de forma {self.climatizacion}")
        print(f"La seguridad del Vehiculo es de forma {self.tipo_seguridad}")
        return "Información adquirida exitosamente"