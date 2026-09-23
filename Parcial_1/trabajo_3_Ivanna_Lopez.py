vidas = 3
inventario = []
escapaste = False


def mostrar_menu():
print("MENU")
print("1. Revisar escritorio")
print("2. Revisar armario")
print("3. Revisar computadora")
print("4. Intentar abrir la puerta")
print("5. Ver inventario")


def escritorio():
print("Revisando el escritorio...")

if "llave" in inventario:
print("Ya buscaste aquí.")
else:
inventario.append("llave")
print("Encontraste una llave.")


def armario():
print("Revisando el armario...")

if "tarjeta" in inventario:
print("Ya buscaste aquí.")
else:
if "llave" in inventario:
print("Usaste la llave y abriste el armario.")
print("Encontraste una tarjeta de acceso.")
inventario.append("tarjeta")
else:
print("El armario está cerrado. Necesitas una llave.")


def computadora():
global vidas

print("Revisando la computadora...")

if "pista" in inventario:
print("Ya buscaste aquí.")
elif "tarjeta" not in inventario:
print("La computadora está bloqueada.")
print("Necesitas una tarjeta de acceso.")
else:
print("La computadora se desbloqueó.")
print("Acertijo:")
print("Tengo números pero no sé contar.")
print("Tengo manecillas pero no tengo manos.")
print("¿Qué soy?")

respuesta = input("Respuesta: ")

if respuesta.lower() == "reloj":
print("¡Correcto! Has conseguido una pista.")
inventario.append("pista")
else:
vidas -= 1
print("Respuesta incorrecta.")
print("Perdiste una vida.")


def abrir_puerta():
global vidas
global escapaste

if "pista" not in inventario:
print("Todavía necesitas encontrar la información necesaria.")
else:
codigo = input("Introduce el código para escapar: ")

if codigo == "1234":
print("¡Correcto!")
print("¡Has escapado del laboratorio!")
escapaste = True
else:
vidas -= 1
print("Código incorrecto.")
print("Perdiste una vida.")


while vidas > 0 and escapaste == False:

print("Vidas restantes:", vidas)

mostrar_menu()

opcion = input("Selecciona una opción: ")

if opcion == "1":
escritorio()

elif opcion == "2":
armario()

elif opcion == "3":
computadora()

elif opcion == "4":
abrir_puerta()

elif opcion == "5":
print("Inventario:", inventario)

else:
print("Opción no válida.")


if vidas == 0:
print("GAME OVER")
print("Te quedaste sin vidas.")

elif escapaste == True:
print("VICTORIA")
print("Lograste escapar del laboratorio.")