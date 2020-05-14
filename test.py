import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame


music_file = "1.mp3"

# while True:
browser = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

browser.get('http://www.nnmarket.co.kr/shop/shopbrand.html?type=M&xcode=025&mcode=001')


try:
    title = WebDriverWait(browser,  3) \
    .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'item-list')))

    # print(title.find_element)
    success = 0
    for item in title:
        name = item.find_element(By.CLASS_NAME, 'prd-brand').text
        if name == '닌텐도 스위치 동물의숲 에디션+ 포켓몬스터 이브이 몬스터볼 SET' or name == 'Nintendo Switch 모여봐요 동물의 숲 에디션' or name == '[스위치]닌텐도 스위치 모여봐요 동물의 숲 에디션+모여봐요 동물의 숲 + 도라에몽 진구의 목장이야기':

            price = item.find_element(By.CLASS_NAME, 'prd-price').text
            if price != 'Sold Out':
                print('엔엔마켓 ㄱㄱㄱㄱ')
                success = 1
    if not success:
        print('구매불가3')
finally:
    browser.quit()


def alert():
    freq = 16000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
    bitsize = -16   # signed 16 bit. support 8,-8,16,-16
    channels = 1    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get right sound)

    # default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    pygame.mixer.quit() 