import requests
import bs4

url = ('http://www.jadwalsholat.pkpu.or.id/?id=203')
conten = requests.get(url)
response = bs4.BeautifulSoup(conten.text ,features="html.parser")
data = response.find_all('tr' , 'table_highlight')
data = data[0]
sholat = {}
i = 0
for datas in data:
        if i == 1:
            sholat['subuh'] = datas.get_text()

        elif i == 2:
            sholat['dhuzur'] = datas.get_text()

        elif i == 3:
            sholat['asar'] = datas.get_text()

        elif i == 4:
            sholat['magrib'] = datas.get_text()

        elif i == 5:
            sholat['isya'] = datas.get_text()
        i+= 1

print(sholat['asar'])



