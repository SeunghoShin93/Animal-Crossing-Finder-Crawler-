import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame

music_file = "1.mp3"   # mp3 or mid file

while True:
    browser = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

    browser.get('https://sofrano.com/product/list.html?cate_no=55')




    try:
        title = WebDriverWait(browser, 3) \
        .until(EC.presence_of_element_located((By.CLASS_NAME, 'prdCount')))
        result = title.text
        if result == '2 ITEMS':
            print('변화 없음')
        else:
            print('소프라노')
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
            # break
    finally:
        browser.quit()

    browser2 = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

    browser2.get('https://smartstore.naver.com/joytronstore/products/4872373481')
    try:
        title = WebDriverWait(browser2,  3) \
        .until(EC.presence_of_element_located((By.CLASS_NAME,  'buy')))
        class_name = title.find_element_by_tag_name('a').get_attribute('class')
        if class_name != '_stopDefault':
            print('조이 트론')
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
            # break
        else:
            print('구매 불가')
    finally:
        browser2.quit()