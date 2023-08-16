#requests : HTTP 통신을 위한 파이썬 라이브러리
#HTTP 통신 : 인터넷에 접속할 때 발생하는 대
#GET요청 : 서버의 리소스에서 데이터를 요청
#POST요청 : 서버의 리소스를 새로 생성하거나 업데이트

import requests
from bs4 import BeautifulSoup

#네이버에서 html 코드 가져오기
response = requests.get("https://www.naver.com") #GET요청
html = response.text #.text에는 html코드가 들어있음

#html 번역하기
soup = BeautifulSoup(html, 'html.parser') #(html 코드, html 번역기)

#원하는 태그 가져오기
word = soup.select_one("#header") #id가 header인 코드 하나 가져오기
print(word.text) #코드 내의 텍스트만 출력

#-------------------------------#

#css : 웹사이트의 디자인을 표시하기 위한 언어
#css 선택자 : 디자인을 변경할 HTML 태그를 선택하는 것 = 크롤링할 HTML 태그를 선택하는 것
#css 선택자의 종류 : 태그 선택자, id 선택자, class 선택자, 자식 선택자
#1. 태그 선택자 : 태그의 이름으로 선택 (h1 태그는 h1, a 태그는 a)
#2. id 선택자 : 원하는 태그를 선택할 수 있음. #id속성값
#3. class 선택자 : 원하는 태그를 선택할 수 있음. .class속성값
#4. 자식 선택자 : 원하는 태그에 별명이 없을 때 사용. 부모태그의 별명(id 또는 class) > 원하는 태그