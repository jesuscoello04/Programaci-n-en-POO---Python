from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio

#Codigo principal
#Aquí va la logica del negocio
#Instancia del padre

objBotella = Botella("Coca_Cola", "1.5L", "Especial")
objBotella.imprimir_info()

#Instancia de la hija Botella_Plastica

objBotella_Plastica = Botella_plastico("Pepsi", "2.5L", "Comun", "Redondo", "plastico", "Sin tinte")
dato_botella_plastica = objBotella_Plastica.imprimir_info()
print(dato_botella_plastica)

#Instancia de la hija Botella_Vidrio

objBotella_Vidrio = Botella_vidrio("Kola Roman", "1.5L", "Comun", "Cubo", "Vidrio", "Roja")
dato_botella_vidrio = objBotella_Vidrio.imprimir_info()
print(dato_botella_vidrio)