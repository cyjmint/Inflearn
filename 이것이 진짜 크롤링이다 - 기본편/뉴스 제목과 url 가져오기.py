#뉴스 제목과 링크 가져오기
import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=삼성전자')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit') #리스트 형태로 출력됨
for link in links:
    title = link.text
    url = link.attrs['href'] #href의 속성값 = url
    print(title,url)