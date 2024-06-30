from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')

time.sleep(3)

#검색어 창을 찾아 search 변수에 저장
search = driver.find_element(By.XPATH, '//input[@id="search"]')


#search 변수에 저장된 곳에 값을 전송
search.send_keys('내맴대로간다')
time.sleep(1)

#search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)


