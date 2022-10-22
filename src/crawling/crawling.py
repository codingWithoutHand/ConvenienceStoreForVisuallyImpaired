import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import (urlopen, urlparse, urlunparse, urlretrieve)
import urllib.request
import os

ITEM = '캔 콜라'
ENG_ITEM = 'CanCoke'
FOLDER = 'CannedDrink'
IMG_COUNT = 500
 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
createFolder(f'./data/{FOLDER}/{ENG_ITEM}')

chrome_path ='chromedriver.exe'
# base_url = "https://www.google.co.kr/imghp"
base_url = f'https://www.google.co.kr/search?q={ITEM}&tbm=isch&source=hp&biw=1036&bih=674&ei=6k5TY9TkDs6c-AaokaSADQ&iflsig=AJiK0e8AAAAAY1Nc-sHpdSsnlZI-pt9bp27m2x-N7NhJ&ved=0ahUKEwjUgZf33vL6AhVODt4KHagICdAQ4dUDCAc&uact=5&oq=%EC%B0%B8%EC%B9%98%EB%A7%88%EC%9A%94+%EC%82%BC%EA%B0%81%EA%B9%80%EB%B0%A5&gs_lp=EgNpbWeKAgtnd3Mtd2l6LWltZ7gBA_gBATIFEAAYgAQyBRAAGIAEMgcQABiABBgYMgcQABiABBgYMgcQABiABBgYwgIIEAAYgAQYsQPCAgsQABiABBixAxiDAcICCBAAGLEDGIMBqAIASKlLUNsLWM9KcAd4AMgBAJABApgBfqAB8hmqAQQyNy44&sclient=img'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("lang=ko_KR") # 한국어
chrome_options.add_argument('window-size=1920x1080')




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(base_url)
driver.implicitly_wait(3)

# #islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# #islrg > div.islrc > div:nth-child(3) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img

last_height = driver.execute_script("return document.body.scrollHeight") #initialize standard of height first
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight") ## update new_height
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() ## click more button
        except:
            break
    last_height = new_height ##last_height update

time.sleep(2)


# #islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# #islrg > div.islrc > div:nth-child(3) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# #islrg > div.islrc > div:nth-child(4) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# #islrg > div.islrc > div:nth-child(94) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
for i in range(2, IMG_COUNT):
    try:
        img = driver.find_element(By.CSS_SELECTOR, f"#islrg > div.islrc > div:nth-child({i}) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")
        imgLink = img.get_attribute("src")
        print(f'[O] Success {i}')
        address = f'./data/{FOLDER}/{ENG_ITEM}'
        urllib.request.urlretrieve(imgLink, f'{address}/{ENG_ITEM}{i}.jpg')
    except:
        print(f'[X] Error {i}')
