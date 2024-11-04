import random

numero_secreto = random.randint(1,101)
cantidad_intentos = 0
#adivinado = False #Quiero tener un booleano para saber si adivino o no
print("Bienvenidos al juego de la vida. En este juego te voy a decir en base a mis conocimientos que tengo sobre vos Guadalupe Quinteros a que edad vas a alcanzar tu plenitud economica ")

while True and cantidad_intentos < 5:

    numero = int(input("Ingresa la edad a la que vos crees que la alcanzarás: ")) #Convertir a numero, por default el ingreso por pantalla es un str.

    if numero == numero_secreto:
        print("Enhorabuena, conseguiras independizarte a los: ", numero)
        break
    elif numero > numero_secreto:
        print("No amiga, me parece que no entendiste bien, proba con una edad mas baja, osea mas joven")
    else:
        print("En serio pensas que estas haciendo las cosas bien como para lograrlo a esta edad?, dale segui intentando con una edad mayor")
    cantidad_intentos += 1
print()
if cantidad_intentos == 5:
    print("Lo siento amiga, volvete al Dolci con la señora Franca")
