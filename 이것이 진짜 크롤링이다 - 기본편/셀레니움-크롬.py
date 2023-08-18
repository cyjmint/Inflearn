import time
import pyautogui
import pyperclip
#셀레니움 기본설정
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

#해당 웹페이지로 주소 이동
driver.get("https://www.naver.com")

#%%네이버 자동 로그인
driver.implicitly_wait(5) #웹페이지가 로딩 될때까지 5초 기다림
driver.maximize_window() #화면 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

#네이버 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR,"#id") #css 선택자의 태그를 자동으로 찾아줌
id.click()
pyperclip.copy("id")
pyautogui.hotkey("command","v")
time.sleep(2)

#네이버 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR,"#pw") 
pw.click()
pyperclip.copy("비밀번호")
pyautogui.hotkey("command","v")
time.sleep(2)

#로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()

#%%
#ValueError: There is no such driver by url https://chromedriver.storage.googleapis.com/LATEST_RELEASE_115.0.5790
#위 오류가 발생했을 때

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://www.naver.com")