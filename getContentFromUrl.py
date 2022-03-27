import requests
import excel
from bs4 import BeautifulSoup
import json

#the array to fill with employee information
list_ce = []

#get data employee to get custom requests
with open("ce.json", "r") as read_file:
        list_ce=json.load(read_file)


# Data we need from the website
parts_surplus_ce = []


#get as many results as needed by each employee with this request loop
for n in list_ce:

    url = "http://xxx.xxx.com/CE_Stock_Status/blackberry_global.asp?ce=" + \
        n["wh"] + "&region=6905&destination=WEB&reportoption=6&excel=False"

    #this conection is posible under vpn connection, if it's fail, the program advice to the user.
    try:
        response = requests.get(url)
        print(">>> Estás conectado a la VPN")
        
        #here we have the html data, we need to grab the custom data using Beautiful soup lib.
        soup = BeautifulSoup(response.text, 'lxml')

        totalUSDSurplus = soup.find("span").text
        print("total surplus: ", totalUSDSurplus)
        
        # This custom webpage has an span html with an 'surplus' id
        surplus = soup.find_all(id="surplus")
        
        #Also we grab another text from the header. 
        header = soup.th.text
        
        print("getting data from ce : ", n["wh"])
       

        #Append data to parts_surplus_ce array.
        for row in surplus:

            tds = row.td.find_next_siblings()

            pn = row.td.text.strip()

            part_name = tds[0].text

            cantidad = tds[2].text

            recibido = tds[3].text

            cost = tds[4].text

            parts_surplus_ce.append(
                [n["wh"], row.a.text.strip(), part_name, cantidad, recibido, cost])
              
        

    #request failed, user is not connected to vpn 
    except requests.exceptions.RequestException as e:
    
        print("No esta conectado a la VPN. Conéctese a la misma y vuelva a ejecutar este archivo")
        input("presione ENTER para cerrar..")
        raise SystemExit(e)


    #calls to createExcel script in excel.py 
    #                (data_array, email_employee, extra_data_employee)
    excel.createExcel(parts_surplus_ce, str(n["mail"]), totalUSDSurplus )
   
    parts_surplus_ce = []


input("press ENTER to close..")
exit()
