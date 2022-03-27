import os
import json

#list all employees from json file
def listar():
   ce=[]
   clear = lambda: os.system('cls')
   clear()

   with open("ce.json", "r") as write_file:
        ce=json.load(write_file)
        if len(ce) == 0:
            print('No hay registros..')
            print('\n presione enter para volver..')
            input()
        else:    
            #iterating through the json list
            for i, x in enumerate(ce):
                print('[',i, '] ', x['name'])
    
        input("Enter to return.. ")
