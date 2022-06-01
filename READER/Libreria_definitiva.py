import csv
user = ""

DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "genre": "Divulgación científica",
    "author": "Antonio Damasio"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_2",
    "title": "El corazón de las tinieblas",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_4",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Las armas y las letras",
    "author": "Andres Trapiello",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]

def get_by_id(id_to_search):
    for book in DB:
        if book["id"] == id_to_search:
            return book
    else:
        print (f"No se ha encontrado el libro con ID {id_to_search}")
        input("\nSiguiente\n")


def pretty_book(book):
    for k,v in book.items():
        print (f"{k} : {v}")
    input("\nSiguiente\n")
        
def get_by_param(user_input, book_param):
    result = []
    user_input = user_input.lower()
    for book in DB:
        if book[book_param].lower().find(user_input) >= 0:
            result.append(book)
    return result

while user != "q":

    print("Bienvenido a la libreria virtual")
    print("1. Buscar por ID")
    print("2. Buscar por Autor")
    print("3. Buscar por Título")
    print("4. Buscar por Genero")
    print("5. Eliminar libro")
    print("6. Modificar libro")
    print("7. Backup")
    print("q. para salir")

    user = input ("Elija opcion: ")

    if user == "1":
        id_to_search = input ("Indique ID del libro: ")
        book = get_by_id(id_to_search)
        if book:
            pretty_book(book)
        
    if user == "2":
        user_input = input("Autor: ")
        user_input = user_input.lower()
        books = get_by_param(user_input, "author")
        if books:
            for book in books:
                pretty_book(book)
        else:
            print("No hay resultados para su busqueda")
            input("\nSiguiente\n")
    
    if user == "3":
        user_input = input("Título: ")
        user_input = user_input.lower()
        books = get_by_param(user_input, "title")
        if books:
            for book in books:
                pretty_book(book)
        else:
            print("No hay resultados para su busqueda")
            input("\nSiguiente\n")    

    if user == "4":
        for i, genre in enumerate(genres):
            print (f"{i + 1}: {genre}")
        user_input = int(input("Introduzca genero: ")) -1
        books = get_by_param (genres[user_input], "genre")
        if books:
            for book in books:
                pretty_book(book)
        else:
            print("No hay resultados para su busqueda")
            input("\nSiguiente\n")

    if user == "5":
        book_to_delete = input ("Introduzca ID de libro a eliminar: ")
        for book in DB:
            if book_to_delete == book["id"]:
                confirmation = input (f"¿Esta seguro que desea eliminar el libro {book['title']}?: \n'y' para confirmar\n: ")
                confirmation = confirmation.lower()
                if confirmation == "y":
                    DB.remove(book)
                    print ("Libro eliminado")
                    input("\nSiguiente\n")
                    break
                else:
                    input("\nVolver al menu principal\n")
        else:
            print("No hay resultados para su busqueda")
            input("\nSiguiente\n")

    if user == "6":
        id_to_search = input ("Introduzca ID de libro a modificar: ")
        book_to_modify = get_by_id(id_to_search)
        if book_to_modify:
            pretty_book(book_to_modify)
            if book_to_modify:
                    new_field = input(f"New {k} ({v}): ")
                    if new_field:
                        book_to_modify[k]=new_field
                        print("Libro modificado")

    
    
    if user == "7":
        file = open("backup.csv", "w", encoding = "utf8", newline="")
        data = csv.writer(file, delimiter=";")
        data.writerow(DB[0].keys())
        for book in DB:
            data.writerow(book.values()) 
        # data.writerow([f"{str(book)}\n" for book in DB])
        file.close()
        print ("Backup realizado")
        