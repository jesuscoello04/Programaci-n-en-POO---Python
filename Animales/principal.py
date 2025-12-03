from modelo_mamifero import Mamifero
from modelo_reptil import Reptil
from modelo_ave import Ave
from modelo_insecto import Insecto
from modelo_pez import Pez

print("\n-------- MAMÍFERO ----------")
caballo = Mamifero("Caballo", 5, "Pradera", "Herbívoro", "Grande", "Café", "Pelaje corto")
caballo.imprimir_informacion()

print("-------- REPTIL --------")
cocodrilo = Reptil("Cocodrilo", 12, "Ríos y pantanos", "Carnívoro", "Grande", "Albino", "Escamas duras")
cocodrilo.imprimir_informacion()

print("-------- PEZ --------")
pez_cirujano = Pez("Pez cirujano", 2, "Arrecifes", "Omnívoro", "Mediano", "Azul", "Agua salada")
pez_cirujano.imprimir_informacion()

print("-------- INSECTO --------")
escarabajo = Insecto("Escarabajo rinoceronte", 1, "Selva", "Detritívoro", "Pequeño", "Negro", 6)
escarabajo.imprimir_informacion()

print("-------- AVE --------")
pato = Ave("Pato silvestre", 3, "Lagos", "Omnívoro", "Mediano", "Blanco y verde", "Pico plano")
pato.imprimir_informacion()
