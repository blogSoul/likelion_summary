import time
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(0.5)