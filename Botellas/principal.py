from modelo_database_botellas import base_datos_botellas
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio

#Codigo principal
#Crear el objeto de la base de datos
obj_base_datos = base_datos_botellas()

#Instancia de la hija Botella_Plastica
objBotella_Plastica = Botella_plastico("Pepsi", "2.5L", "Comun", "Redondo", "plastico", "Sin tinte")

#Instancia de la hija Botella_Vidrio
objBotella_Vidrio = Botella_vidrio("Kola Roman", "1.5L", "Comun", "Cubo", "Vidrio", "Roja")

#Guardar informacion en la base de datos
obj_base_datos.guardar_objeto(objBotella_Plastica)
obj_base_datos.guardar_objeto(objBotella_Vidrio)

#Mostrar la informacion
obj_base_datos.imprimir_info()