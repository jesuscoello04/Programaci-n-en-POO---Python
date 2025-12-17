from modelo_database_vehiculos import base_datos_vehiculos
from modelo_vehiculo_deportivo import Vehiculo_Deportivo
from modelo_vehiculo_transporte import Vehiculo_Transporte
from modelo_vehiculo_carga import Vehiculo_Carga

#Codigo principal
#Crear el objeto de la base de datos
obj_base_datos = base_datos_vehiculos()

#Instancia de la hija vehiculo_deportivo
objVehiculo_deportivo = Vehiculo_Deportivo(
    "BMW Z4 Roadster", "3.0L TwinPower Turbo (6 cilindros)", "Gris metalico",
    "Boton de encendido", "Boton Start/Stop",
    "Climatizador bizona automático", "Llave inteligente (Keyless)"
)

#Instancia de la hija vehiculo_transporte
objVehiculo_transporte = Vehiculo_Transporte(
    "JAC Sunray Passenger Van", "Blanco polar", "Motor 2.0L Turbo Diésel",
    "Llave tradicional", "Giro manual en el switch",
    "Aire acondicionado de cabina completa", "Cierre centralizado"
)

#Instancia de la hija vehiculo_carga
objVehiculo_carga = Vehiculo_Carga(
    "JAC Heavy Duty Truck", "Blanco estándar", "Motor 3.8L Turbo Diésel",
    "Llave tradicional reforzada", "Apagado manual por switch",
    "Aire acondicionado básico de cabina", "Cierre mecánico"
)

#Guardar informacion en la base de datos
obj_base_datos.guardar_objeto(objVehiculo_deportivo)
obj_base_datos.guardar_objeto(objVehiculo_transporte)
obj_base_datos.guardar_objeto(objVehiculo_carga)

#Mostrar la informacion
obj_base_datos.imprimir_info()