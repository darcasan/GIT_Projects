import random as rdm

user = ""
choices = ["Piedra", "Papel", "Tijeras"]

print ("Bienvenido a piedra, papel o tijeras:")
input("Pulsa cualquier 'Enter' para empezar")

while user.lower != "q":

    print ("Elige una opción:\n")
    print ("1. Piedra")
    print ("2. Papel")
    print ("3. Tijera")
    print ("q. Para salir")

    user = input("Introduce opción: ")

    if user == "1":
        print ("\nHas elegido Piedra")
        pc_choice = rdm.choice(choices)
        print (f"IA Elige {pc_choice}")
        if pc_choice == choices[0]:
            print ("Empate")
            input("\nsiguiente\n")
        elif pc_choice == choices[1]:
            print ("Has perdido")
            input("\nsiguiente\n")
        elif pc_choice == choices[2]:
            print ("Has ganado")
            input("\nsiguiente\n")

    if user == "2":
        print ("\nHas elegido Papel")
        pc_choice = rdm.choice(choices)
        print (f"IA Elige {pc_choice}")
        if pc_choice == choices[0]:
            print ("Has ganado")
            input("\nsiguiente\n")
        elif pc_choice == choices[1]:
            print ("Empate")
            input("\nsiguiente\n")
        elif pc_choice == choices[2]:
            print ("Has perdido")
            input("\nsiguiente\n")

    if user == "3":
        print ("\nHas elegido Tijera")
        pc_choice = rdm.choice(choices)
        print (f"IA Elige {pc_choice}")
        if pc_choice == choices[0]:
            print ("Has perdido")
            input("\nsiguiente\n")
        elif pc_choice == choices[1]:
            print ("Has ganado")
            input("\nsiguiente\n")
        elif pc_choice == choices[2]:
            print ("Empate")
            input("\nsiguiente\n")
    
    if user == "q":
        break