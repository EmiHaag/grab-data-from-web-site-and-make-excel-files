import requests
import excel
from bs4 import BeautifulSoup
import json

#list_ce = [{"wh": "AR903E46", "mail": "eh185079"},{"wh": "AR903E84", "mail": "AP185390"},{"wh": "AR903E39", "mail": "JP250221"},{"wh": "AR903E82", "mail": "GT250050"},{"wh": "AR903E83", "mail": "FC185079"}]
list_ce = []
with open("ce.json", "r") as read_file:
        list_ce=json.load(read_file)


# tabla partes en surplus
parts_surplus_ce = []

for n in list_ce:

    url = "http://fls.ncr.com/CE_Stock_Status/blackberry_global.asp?ce=" + \
        n["wh"] + "&region=6905&destination=WEB&reportoption=6&excel=False"

    #parts_surplus_ce.append(["Legajo", "Part number", "Part name", "Cantidad", "Fecha", "$COST"])
    try:
        response = requests.get(url)
        print(">>> Estás conectado a la VPN")

        soup = BeautifulSoup(response.text, 'lxml')

        totalUSDSurplus = soup.find("span").text
        print("total surplus: ", totalUSDSurplus)
        # obtiene elemento html con id "surplus"
        surplus = soup.find_all(id="surplus")
        header = soup.th.text
        print("getting data from ce : ", n["wh"])
        # analiza la pagina scrapeada actual y crea objeto con datos de pn en surplus
       


        for row in surplus:

            tds = row.td.find_next_siblings()

            pn = row.td.text.strip()

            part_name = tds[0].text

            cantidad = tds[2].text

            recibido = tds[3].text

            cost = tds[4].text

            parts_surplus_ce.append(
                [n["wh"], row.a.text.strip(), part_name, cantidad, recibido, cost])
            print("td: ", tds[4].text, " to ce: ", n["wh"])
        print("end ce:", n["wh"], "=======================================")
       
        

    except requests.exceptions.RequestException as e:
    
        print("No esta conectado a la VPN. Conéctese a la misma y vuelva a ejecutar este archivo")
        input("presione ENTER para cerrar..")
        raise SystemExit(e)


    print("creating excel file for "+ n["wh"] + ".. wait.")
    excel.createExcel(parts_surplus_ce, str(n["mail"]), totalUSDSurplus )
   
    parts_surplus_ce = []


input("press ENTER to close..")
exit()
