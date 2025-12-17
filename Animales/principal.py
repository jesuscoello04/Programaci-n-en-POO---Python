from modelo_database_animales import base_datos_animales
from modelo_mamifero import Mamifero
from modelo_reptil import Reptil
from modelo_ave import Ave
from modelo_insecto import Insecto
from modelo_pez import Pez

# Crear la base de datos
#Crear el objeto de la base de datos
obj_base_datos = base_datos_animales()

#Instancia de la hija mamifero
objMamifero = Mamifero("Caballo", 5, "Pradera", "Herbívoro", "Grande", "Café", "Pelaje corto")

#Instancia de la hija mamifero
objReptil = Reptil("Cocodrilo", 12, "Ríos y pantanos", "Carnívoro", "Grande", "Albino", "Escamas duras")

#Instancia de la hija mamifero
objPez = Pez("Pez cirujano", 2, "Arrecifes", "Omnívoro", "Mediano", "Azul", "Agua salada")

#Instancia de la hija mamifero
objInsecto = Insecto("Escarabajo rinoceronte", 1, "Selva", "Detritívoro", "Pequeño", "Negro", 6)

#Instancia de la hija mamifero
objAve = Ave("Pato silvestre", 3, "Lagos", "Omnívoro", "Mediano", "Blanco y verde", "Pico plano")

#Guardar informacion en la base de datos
obj_base_datos.guardar_objeto(objMamifero)
obj_base_datos.guardar_objeto(objReptil)
obj_base_datos.guardar_objeto(objPez)
obj_base_datos.guardar_objeto(objInsecto)
obj_base_datos.guardar_objeto(objAve)

# Imprimir toda la información
obj_base_datos.imprimir_info()