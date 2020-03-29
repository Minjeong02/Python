from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = bs(html.text,'html.parser')
html.close()

data1 = soup.find('div',{'class':'list_area daily_all'})  
#pprint(data1)

data2 = soup.find('div',{'class':'col col_selected'}) 
#pprint(data2)

#data3 = data2.findAll('a',{'class':'title'})

#for i in data3:
    #print(i.text)

#data4 = soup.find('div',{'class':'col_inner']})

#data5 = data4.findAll('a',{'class':'title'})

#for i in data5:
    #print(i.text)


data2 = data1.findAll('div',{'class':'col_inner'}).text
for i in data2:
    data3 = i.findAll('a',{'class':'title'})
    pprint(data3)
    for j in data3 :
        print(j.text)