import time
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(0.5)

driver.find_element_by_css_selector('input#id').send_keys('input_the_id')
time.sleep(1)
driver.find_element_by_css_selector('input#pw').send_keys('input_the_pw')
time.sleep(1)
driver.find_element_by_css_selector('input.btn_global').click()