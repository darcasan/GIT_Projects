# file = open("test.txt")
# file = open("test.txt", "r") - Permite leer
# file = open("test.txt", "w") - Permite escribir
file = open("test.txt", "a")
file.write("Cambio de file")
file.write("\nPepi Pache")

file.close()