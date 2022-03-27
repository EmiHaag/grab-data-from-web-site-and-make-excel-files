import os
import listCE
import add_ce
import remove_ce


selected = 100

def displayMenu():
 
    global selected
    clear = lambda: os.system('cls')
    clear()

    print('SURPLUS - NCR LIST')
    print('=========================================\n')

    print("List, Add or remove from CE's \n")
    print("0- List CE's")
    print("1- Add CE")
    print("2- Remove CE \n")
    print('3- execute query')
    print("9- exit")

    print('=========================================\n')

    selected = int(input("Seleccione opcion"))

    if selected == 0:
        listCE.listar()
    elif selected == 1:
        add_ce.add_CE()
    elif selected == 2:
        remove_ce.removeCE()
    elif selected == 3:
        exec(open('getContentFromUrl.py').read())
    elif selected == 9:
        print("exit.. ")

while(selected != 9): displayMenu()
