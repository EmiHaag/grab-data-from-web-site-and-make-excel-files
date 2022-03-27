import json
import os

#list employees, select one and remove it from employees json file
def removeCE():
    
    #open json file
    f = open('ce.json')
    data = []
    selected = -1


    #open file once for reading and close it.
    with open('ce.json', "r") as jsonFile:
        data=json.load(jsonFile)

    def list_ce():
        clear = lambda: os.system('cls')
        clear()
        
        if len(data) == 0:
            print('No hay registros..')
            print('\n presione enter para volver..')
            input()
        else:    
            #iterating through the json list
            for i, x in enumerate(data):
                print('[',i, '] ', x['name'], x['wh'])
            print('Seleccione num de ce a eliminar de la lista de ce \n ')
            print('\n (-1 para volver)')

            while True:
                selected = input("Ingrese un numero")
                #Catch only numbers
                try:
                    selected = int(selected)
                except ValueError:
                    print('Ingrese un numero valido')
                    continue
                if selected > -1:
                    delete_from_data(selected)
                else:
                    print("exit.. ")
                    break



    def delete_from_data(ind):
        print('type: ', type(data[ind]))

        #delete from memory 
        del data[ind]
        
        print('deleting from data', )

        #update json file   
        with open("ce.json", "w") as write_file:
            json.dump(data, write_file)

        input('ce borrado.. press enter')
        list_ce()



    list_ce()



