import time
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://comic.naver.com/webtoon/list.nhn?titleId=729037&weekday=sun&page=1')
time.sleep(2)
for i in range(5):
    titles = driver.find_elements_by_css_selector('td.title a')
    button = driver.find_elements_by_css_selector('a.next')
    for title in titles:
        print(title.text)
    button.click()

#The problem is that you are using find_element_by_xpath which return only one WebElement (which is not iterable), the find_elements_by_xpath return a list of WebElements.
#Solution: replace find_element_by_xpath with find_elements_by_xpath