import time

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait

# options = Options()
# options.headless = True
import pygame

music_file = "1.mp3"   # mp3 or mid file

while True:
    browser = webdriver.Chrome("C:/Users/ficd0/Desktop/새 폴더/chromedriver.exe")

    browser.get('https://sofrano.com/product/list.html?cate_no=55')
    

    time.sleep(1)

    tag_name = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[4]/div[1]/div/p/strong')


    result = tag_name.text
    browser.quit()
    print(result)
    if result != '2':
        print('떳다')
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
        break

# for tag in tag_name:
#     print(tag.text.split("\n"))

