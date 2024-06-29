from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=2&acq=%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8')
# pprint(html.text)

soup = bs(html.text,'html.parser')

data1 = soup.findAll('li', {'class':'item_today level1'})
pprint(data1)

title_dust = data1[0].find('strong',{'class':'title'}).text
find_dust = data1[0].find('span',{'class':'txt'}).text

title_ultra_dust = data1[1].find('strong',{'class':'title'}).text
ultra_find_dust = data1[1].find('span',{'class':'txt'}).text

title_uv = data1[2].find('strong',{'class':'title'}).text
find_uv = data1[2].find('span',{'class':'txt'}).text

pprint(title_dust)
print(title_dust, ":",find_dust)
print(title_ultra_dust,":",ultra_find_dust)
print(title_uv,":",find_uv)