import json
import os

#add employee data to json file array of objects
def add_CE():
    ce = []

    clear = lambda: os.system('cls')
    clear()

    with open("ce.json", "r") as write_file:
        ce=json.load(write_file)


    name = input("Nombre: ")
    wh = input("Warehouse: ")
    mail = input("QuickLookID: ")

    print(name, wh, ", ", mail, ", ")

    ce.append({
        "name":name, 
        "wh": wh,
        "mail":mail})

    with open("ce.json", "w") as write_file:
        json.dump(ce, write_file)

        
    input("press enter.. ")
