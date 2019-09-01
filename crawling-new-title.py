import time
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://comic.naver.com/webtoon/list.nhn?titleId=729037&weekday=sun&page=1')
time.sleep(2)
for i in range(5):
    titles = driver.find_element_by_css_selector('td.title a')
    button = driver.find_element_by_css_selector('a.next')
    for title in titles:
        print(title.text)
    button.click()