#Clase Padre Vehiculo

class Vehiculo():
    def __init__(self, modelo, color, motor, metodo_arranque, metodo_apagado):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.metodo_arranque = metodo_arranque
        self.metodo_apagado = metodo_apagado

    def aceleracion(self):
        return "El vehiculo acelera de manera gradual"
    
    def frenado(self):
        return "El vehiculo reduce su velocidad de manera gradual"

    def imprimir_informacion(self):
        print(f"El modelo del vehiculo es: {self.modelo}")
        print(f"El color del vehiculo es: {self.color}")
        print(f"El modelo del vehiculo es: {self.motor}")
        print(f"El metodo de arranque del vehiculo es: {self.metodo_arranque}")
        print(f"El metodo de apagado del vehiculo es: {self.metodo_apagado}")
