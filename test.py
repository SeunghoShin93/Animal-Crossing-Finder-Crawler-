import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame


music_file = "1.mp3"

# while True:
browser = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

browser.get('http://display.cjmall.com/p/item/64124263?channelCode=30001001#')


try:
    title = WebDriverWait(browser,  3) \
    .until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[2]/a')))
    
    sold_out = title.text

    if sold_out == '매진':
        print('구매 불가4')
    else:
        alert()




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