import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

data_list = list()
header = list()
header.append("Nr. crt.")
header.append("Județ")

first = True

for day in range(3, 25):
    string1 = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-'

    if day == 7 or day == 17:  #pentru 7 si 17 url-ul se formeaza altfel
        string2 = '-aprilie-2020-ora-13-00-2/'
        req = requests.get(string1 + str(day - 1) + string2)
    else:
        string2 = '-aprilie-2020-ora-13-00/'
        req = requests.get(string1 + str(day) + string2)

    response = req.text
    link = BeautifulSoup(response, 'html.parser')
    title = link.find_all('div', attrs={'class': 'entry-content'})

    header.append(str(day) + " Aprilie")
    for i in title:
        for tr_index in i.find_all('table', limit=1):  #in div se gasesc 2 tabele
            index = 0
            for td_index in tr_index.find_all('tr', limit=43)[1:]:  #primul element TR reprezenta capul de tabel
                list_td = list()

                for trd_index in td_index.find_all('td'):
                    list_td.append(trd_index.get_text().lstrip(' '))

                if first:  #din primul link luam toate elementele din tabel
                    data_list.append(list_td)
                else:  #din urmatoarele luam doar coloana cu numar de cazuri
                    data_list[index].append(list_td[2])

                index += 1
    first = False

#construiesc din lista finala de date -> string pentru html
tr = ''
for index in range(42):
    td = ''
    for element in data_list[index]:
        td += f'<td>{element}</td>'
    data_list[index] = tuple(data_list[index])
    tr += f'<tr>{td}</tr>'

header_html = ''
for element in header:
    header_html += f'<th>{element}</th>'

thead = f'<thead><tr>{header_html}</tr></thead>'
table = f'<table>{thead}<tbody>{tr}</tbody></table>'

#HTML
print(table)
with io.open('COVID.html', "w", encoding="utf-8") as file:
    file.writelines(table)
    file.close()

#EXCEL
print(data_list)
print(header)
df = pd.DataFrame(data_list, columns=header)
df.to_excel('COVID.xls', sheet_name='C19', header=header, index=0)
