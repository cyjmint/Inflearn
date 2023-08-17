#여러 페이지의 결과 가져오기
import requests
from bs4 import BeautifulSoup
import pyautogui

lastpage = pyautogui.prompt('마지막 페이지 번호를 입력')
num = 1
for i in range(1,int(lastpage)*10,10):
    print(f'------------{num}페이지입니다.------------')
    response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=삼성전자&start={i}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.news_tit') #리스트 형태로 출력됨
    for link in links:
        title = link.text
        url = link.attrs['href'] #href의 속성값 = url
        print(title,url)
    num += 1