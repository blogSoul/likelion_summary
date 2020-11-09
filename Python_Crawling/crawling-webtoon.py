import time
from selenium import webdriver
import pymysql

conn =pymysql.connect(
    host='localhost',
    user='root',
    password='비밀번호',
    db='DB이름',
    charset='utf8'
)

cursor = conn.cursor()

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://comic.naver.com/webtoon/list.nhn?titleId=729037&weekday=sun&page=1')
time.sleep(2)

titles = driver.find_elements_by_css_selector('td.title a')

for title in titles:
    print(title.text)
    SQL = "INSERT INTO `comments`(`title`, `url`) VALUES ('%s', '%s')" % (title.text, title.get_attribute('href'))
    cursor.execute(SQL)

conn.commit()

#The problem is that you are using find_element_by_xpath which return only one WebElement (which is not iterable), the find_elements_by_xpath return a list of WebElements.
#Solution: replace find_element_by_xpath with find_elements_by_xpath