import random
from random import randint #Importa solo la funcion indicada
from random import * #Importa todas las funciones en random (no es necesario escrbir random.funcionausar)

print (random.randint(0, 100))

choices = ["rock", "paper", "scissors", "lizard", "spock"]

print(random.choice(choices))