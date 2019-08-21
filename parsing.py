import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com').text

soup = BeautifulSoup(response, 'html.parser')
tags = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

for x in tags:
    print(x.text)