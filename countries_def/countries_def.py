from tkinter import CENTER
import requests as req
import sys
import json
import os
import random as rd

CWD = os.getcwd()

def clear():
    if os.name == "nt":
        os.system("cls")
        return None

def get_data_country():
    ctry_to_search = input("Input country to search: ")
    clear() 
    print(f"{ctry_to_search} information: \n".center(50))
    url = f"https://restcountries.com/v3.1/name/{ctry_to_search}?fullText=true"
    data = req.get(url).json()
    ctry_list = []
    keys = ["Capital", "Population", "Area", "Languages"]
    for country in data:
        if ctry_to_search == country["name"]["common"]:
            ctry_list.append(country["capital"][0])
            ctry_list.append(country["population"])
            ctry_list.append(country["area"])
            ctry_list.append(list(country["languages"].values()))
            final_list = zip(keys,ctry_list)
            return (final_list)

def get_flag():
    ctry_to_search = input("Input country to download flag: ")
    url = f"https://restcountries.com/v3.1/name/{ctry_to_search}?fullText=true"
    data = req.get(url).json()
    for ctry in data:
        if ctry_to_search == ctry["name"]["common"]:
            flag = ctry["flags"]["png"]
    flag = req.get(flag).content
    flag_file = open(f"{CWD}/flags/{ctry_to_search}.png", "wb")
    flag_file.write(flag)
    flag_file.close()
    return ("Ok")
    
def countries_game():
    questions = [
        {
            "q": "How big is the area of *@*?",
            "answer": "*@*",
            "key": "area",
            "options": []
        },
        {   
            "q": "What's the population of *@*?",
            "answer": "*@*",
            "key": "population",
            "options": []
        },
        {
            "q": "Is *@* independent?", 
            "answer": "*@*",
            "key": "independent",
            "options": []
        },
        {
            "q": "Is *@* a member of the UN?",
            "answer": "*@*",
            "key": "unMember",
            "options": []
        },
        {
            "q": "¿Which one is the capital of *@*", 
            "answer": "*@*",
            "key": "capital",
            "options": []
        }
    ]


    continent_list = ["Africa", "Americas", "Asia", "Europe", "Oceania"]
    print ("Country game!\n")
    print ("Choose a continent")
    for k, i in enumerate(continent_list):
        print (f"{k+1} - {i}")
    user_cont = (input(": "))
    while user_cont not in ("1", "2", "3", "4", "5"):
        print ("Please select a valid number")
        user_cont = input ("Your choice: ")
    user_cont = int(user_cont)
    clear()
    print (f"You've chosen {continent_list[user_cont-1]}")
    input ("Press 'Enter' to cotinue")
    clear()
    url =f"https://restcountries.com/v3.1/region/{continent_list[user_cont-1]}"
    res = req.get(url).json()
    data = list(res)

    country_list = []
    for i in data:
        n = rd.randint(0,len(data)-1)
        if data[n] not in country_list:
            if data[n].get("capital") and data[n].get("independent"):
                country_list.append(data[n])
        else:
            pass
        if len(country_list)==5:
            break

    i = 0
    for question in questions:
        question["q"] = question["q"].replace("*@*", country_list[i]["name"]["common"])
        question["answer"] = question["answer"].replace("*@*", str(country_list[i][question["key"]]))
        for country in country_list:
            question["options"].append(country[question["key"]])
        i += 1

    score = 0

    question = rd.shuffle(questions)
    for q in questions:
        print (q["q"])
        if type(q["options"][0]) == bool:
            q["options"].clear()
            q["options"].append(True)
            q["options"].append(False)
            print ("1 - True\n2 - False")
            answer = input ("Your choice: ")
            while answer not in ("1", "2","q"):
                print ("Please select a valid number")
                answer = input ("Your choice: ")
            if answer == "q":
                break                    
            answer = int(answer)-1
            if str(q["options"][answer]) == q["answer"]:
                print ("That's right!")
                input ("")
                clear()
                score +=2
            elif q["options"][answer] != q["answer"]:
                print (f"Wrong, the answer was: {q['answer']}")
                input ("")
                clear()
        else:
            for k, i in enumerate(q["options"]):
                print (f"{k+1} - {i}")
            answer = input ("Your choice: ")
            while answer not in ("1", "2", "3", "4", "5","q"):
                print ("Please select a valid number")
                answer = input ("Your choice: ")
            if answer == "q":
                break               
            answer = int(answer)-1
            if str(q["options"][answer]) == q["answer"]:
                print ("That's right!")
                input ("")
                clear()
                score +=2
            elif q["options"][answer] != q["answer"]:
                print (f"Wrong, the answer was: {q['answer']}")
                input ("")
                clear()

    input ("Press 'Enter' to cotinue")
    clear()
    print(f"Your score was {score}/10")
    input ("Press 'Enter' to cotinue")
    clear()
        
    

user = ""
while user != "q":

    print ("1. To search by country".center(50))
    print ("2. To download a flag".center(50))
    print ("3. To play".center(50))
    print ("q. To exit".center(50))

    user = input ("\nUser choice:")
    
    if user == "1":
        clear()
        ctry = get_data_country()
        for k, i in ctry:
            print (f"{k}: {i}")
        input(":")
        clear()

    if user == "2":
        clear()
        get_flag()

    if user == "3":
        clear()
        countries_game()
    
