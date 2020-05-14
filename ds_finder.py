import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame

music_file = "1.mp3"   # mp3 or mid file

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


while True:

    # 소프라노

    browser = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

    browser.get('https://sofrano.com/product/list.html?cate_no=55')


    try:
        title = WebDriverWait(browser, 3) \
        .until(EC.presence_of_element_located((By.CLASS_NAME, 'prdCount')))
        result = title.text
        if result == '2 ITEMS':
            print('구매 불가1')
        else:
            print('소프라노 ㄱㄱㄱ')
            alert()
            break
    finally:
        browser.quit()

    # 조이트론

    browser2 = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

    browser2.get('https://smartstore.naver.com/joytronstore/products/4872373481')
    try:
        title = WebDriverWait(browser2,  3) \
        .until(EC.presence_of_element_located((By.CLASS_NAME,  'buy')))
        class_name = title.find_element_by_tag_name('a').get_attribute('class')
        if class_name != '_stopDefault':
            print('조이 트론 ㄱㄱㄱㄱ')
            alert()
            break
        else:
            print('구매 불가2')
    finally:
        browser2.quit()

    # 엔엔마켓

    browser3 = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

    browser3.get('http://www.nnmarket.co.kr/shop/shopbrand.html?type=M&xcode=025&mcode=001')

    try:
        title = WebDriverWait(browser3,  3) \
        .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'item-list')))

        # print(title.find_element)

        for item in title:
            name = item.find_element(By.CLASS_NAME, 'prd-brand').text
            if name == '닌텐도 스위치 동물의숲 에디션+ 포켓몬스터 이브이 몬스터볼 SET' or name == 'Nintendo Switch 모여봐요 동물의 숲 에디션' or name == '[스위치]닌텐도 스위치 모여봐요 동물의 숲 에디션+모여봐요 동물의 숲 + 도라에몽 진구의 목장이야기':

                price = item.find_element(By.CLASS_NAME, 'prd-price').text
                if price != 'Sold Out':
                    print('엔엔마켓 ㄱㄱㄱㄱ')
                    alert()
 
                    break
        
        print('구매 불가3')
    finally:
        browser3.quit()