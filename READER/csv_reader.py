import csv

file = open("test.csv", "a")
data = csv.writer(file)
data.writerow(["003", "punbike", 14, 1300])

# print(next(data, "No hay mas bicis")) Imprime la primera iterable 
# print(next(data, "No hay mas bicis")) Imprime la segunda iterable 
# print(next(data, "No hay mas bicis")) xxxxx
# print(next(data, "No hay mas bicis"))
# print(next(data, "No hay mas bicis"))

# Los csv son un Iterator (Se usan una vez y luego se vacian), si lo convertimos en list se convierte en un iterable (Se usa todas las veces que queramos)
#Si no aparecen tildes, agregar despues de open("fichero", encoding="utf8")

# for bike in data:
#     print (bike)

