from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt

browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2019.htm')
table = browser.find_element_by_xpath('//*[@id="Data_table"]')

#TXT
fisier = open('BNR_ALL.txt', 'w+')
fisier.writelines(table.text)
fisier.close()

tabel = table.text
lista = tabel.split('\n')

header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')

dictionar = {i: [] for i in header}

for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        if '-' in lista[i]:
            dictionar[header[int(j)]].append(lista[i])
        else:
            dictionar[header[int(j)]].append(float(lista[i]))

#EXCEL
df = pd.DataFrame(dictionar)
df.to_excel("BNR_ALL.xls", sheet_name='BNR', header=header, index=0)

browser.close()

a = header[3:9]
c = []
for i in range(3, 9):
    c.append(dictionar[header[int(i)]][int(i)])
d = sum(c)
e = []
for item in c:
    e.append(round(item/d*100))

colors = ['r', 'y', 'g', 'b', 'g', 'y']

plt.pie(e, labels=a, colors=colors, startangle=90, shadow=True, explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.2), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.show()
