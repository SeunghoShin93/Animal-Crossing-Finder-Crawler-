import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame

chrome_path= "D:/Download/chromedriver_win32/chromedriver.exe"

music_file = "1.mp3"
cnt = 1
# while True:

def browser_form(domain):
    global cnt
    globals()['browser'+str(cnt)] = webdriver.Chrome(chrome_path)
    globals()['browser'+str(cnt)].get(domain)
    cnt += 1

browser_form('https://smartstore.naver.com/joytronstore/category/0cdf08e497434eb4b46d4e039ef504d4?cp=1')

# globals()['browser'+str(cnt)] = webdriver.Chrome("D:/Download/chromedriver_win32/chromedriver.exe")

# globals()['browser'+str(cnt)].get('http://display.cjmall.com/p/item/64124263?channelCode=30001001#')


try:
    title = WebDriverWait(browser1,  3) \
    .until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/form/div[3]/ul/li[6]/div[3]')))
    
    sold_out = title.text

    print(sold_out)
    # if sold_out == '매진':
    #     print('구매 불가4')
    # else:
    #     print('구매 가능')



finally:
    browser1.quit()


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