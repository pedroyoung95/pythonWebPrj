from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://novel.naver.com/webnovel/weekday')

soup = bs(html.text, 'html.parser')
html.close()

data1 = soup.find('div', {'class':'component_section'})

data2 = data1.findAll('span', {'class':'title'})

pprint(data2)
