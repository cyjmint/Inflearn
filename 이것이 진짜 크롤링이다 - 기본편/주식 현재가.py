import requests
from bs4 import BeautifulSoup
from numbers_parser import Document

#주식 현재가 number에 저장하기
doc = Document('abcde.numbers')
sheets = doc.sheets
tables = sheets[0].tables
table = tables[0]
sheets[0].name = '주식현재가 크롤링'
tables[0].name = '주식현재가'
table.write('A1','종목번호')
table.write('B1','주식명')
table.write('C1','현재가')

codes = ['005930','000660','035720', '005490']
row = 2
for code in codes:
    url = f'https://finance.naver.com/item/sise.naver?code={code}'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal').text
    price = price.replace(',', '')
    table.write(f'C{row}',price)
    row += 1

for i in range(len(codes)):
    table.write(f'A{i+2}',codes[i])
    
doc.save('주식현재가.numbers')
