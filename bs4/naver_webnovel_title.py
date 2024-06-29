import errno

from bs4 import BeautifulSoup as bs
from pprint import pprint
from urllib.request import urlretrieve
import requests, re, os

#저장 폴더 생성
try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

#웹 페이지 읽고 소스코드 읽기
html = requests.get('https://novel.naver.com/webnovel/weekday')
soup = bs(html.text, 'html.parser')
html.close()

#웹소설 통합랭킹 영역 추출
data1_list = soup.findAll( 'ul', {'class':'ranking_list type1 NE=a:all'})

#통합랭킹 웹소설
novel_list = []
for data1 in data1_list:
    #웹소설 썸네일 및 제목 영역 추출
    novel_list.extend(data1.findAll('li'))

#각각의 썸네일과 제목 추출
for novel in novel_list:
    img = novel.find('img')
    title = img['alt']
    img_src = img['src']
    title = re.sub('[^0-9a-zA-zㄱ-힗]','', title)
    urlretrieve(img_src, './image/'+title+'.jpg')