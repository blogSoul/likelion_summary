import time
from selenium import webdriver

#네이버 생활뉴스 랭킹 30 제목 크롤링하기
driver = webdriver.Chrome('C:/chromedriver.exe')
news_home = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20190526'
data = []
driver.get(news_home)
time.sleep(2)

titles = driver.find_elements_by_css_selector('div.ranking_headline a')
title_list = []
url_list = []

for title in titles:
    title_list.append(title.text)
    url_list.append(title.get_attribute('href'))

for i in range(len(url_list)):
    dic = {}
    comment_list = []
    driver.get(url_list[i])
    time.sleep(0.5)
    comments = driver.find_elements_by_css_selector('span.u_cbox_contents')
    for comment in comments:
        comment_list.append(comment.text)

    dic["title"] = title_list[i]
    dic["url"] = url_list[i]
    dic["comment"] = comment_list
    comment_list = []
    print(dic)

    data.append(dic)