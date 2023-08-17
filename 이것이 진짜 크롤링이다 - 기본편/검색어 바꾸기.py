import requests
from bs4 import BeautifulSoup
import pyautogui

#url : 인터넷 주소 형식, protocol - domain - path - parameter
#https: : protocol
#//search.naver.com : domain, ip 주소에 이름을 준 것
#/search.naver : path, 서버에서 해당 페이지의 경로
#?where=news&sm=tab_jum&query=삼성전자 : parameter, key = value 형태로 구성되어 있으며 &로 이어짐, 서버에 추가적인 정보 제공
#parameter에서 query의 value 값이 검색어

#검색어 변경하기
#1. input() 사용
keyword = input('검색어를 입력하세요 >>>')
response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+keyword)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit') #리스트 형태로 출력됨
for link in links:
    title = link.text
    url = link.attrs['href'] #href의 속성값 = url
    print(title,url)

#2. pyautogui 사용
#pyautogui : 마우스, 키보드 매크로 라이브러리. 
keyword = pyautogui.prompt('검색어를 입력하세요 >>>') #간단한 입력창 띄우기
response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit') #리스트 형태로 출력됨
for link in links:
    title = link.text
    url = link.attrs['href'] #href의 속성값 = url
    print(title,url)