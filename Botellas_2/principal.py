from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico

#Codigo principal
#Aquí va la logica del negocio
#Instancia del padre

objBotella = Botella("Coca_Cola", "1.5L", "Especial")
objBotella.imprimir_info()
#Instancia de la hija

objBotella_Plastica = Botella_plastico("Pepsi", "Personal", "Comun", "Redondo", "plastico", "Sin tinte")
dato_out = objBotella_Plastica.imprimir_info()
print(dato_out)