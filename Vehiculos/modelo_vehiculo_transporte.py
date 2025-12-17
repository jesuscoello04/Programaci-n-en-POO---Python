from modelo_vehiculo import Vehiculo

#Clase Hija de Vehiculo_Transporte

class Vehiculo_Transporte(Vehiculo):
    def __init__(self, modelo, color, motor, metodo_arranque, metodo_apagado, climatizacion, tipo_seguridad):
        super().__init__(motor, color, modelo, metodo_arranque, metodo_apagado)
        self.climatizacion = climatizacion
        self.tipo_seguridad = tipo_seguridad
        
    def abrir_puerta_corrediza(self):  
        return "La puerta se ha abierto correctamente"
    
    def cerrar_puerta_corrediza(self):  
        return "La puerta se ha cerrado correctamente"
    
    def recoger_pasajero(self, cantidad):
        return f"Se han recogido {cantidad} pasajeros."
    
    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"La climatización del Vehiculo {self.modelo} es de forma {self.climatizacion}")
        print(f"La seguridad del Vehiculo {self.modelo} es de forma {self.tipo_seguridad}")