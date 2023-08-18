#safai 브라우저는 기본적으로 webdriver가 내장되어 있음
#그러므로 chrome이나 firefox같이 브라우저 버전에 맞는 driver를 다운로드하여 $PATH 부분에 넣어줄 필요가 없음
#safari는 개발자용 탭에서 '원격 자동화 허용'만 설정해주면 됨
import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

#해당 웹페이지로 주소 이동
browser = webdriver.Safari()
browser.maximize_window()
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

#네이버 아이디 입력창
id = browser.find_element(By.CSS_SELECTOR,"#id") #css 선택자의 태그를 자동으로 찾아줌
id.click()
pyperclip.copy("id")
pyautogui.hotkey("command","v")
time.sleep(2)

#네이버 비밀번호 입력창
pw = browser.find_element(By.CSS_SELECTOR,"#pw") 
pw.click()
pyperclip.copy("비밀번호")
pyautogui.hotkey("command","v")
time.sleep(2)

#로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()
