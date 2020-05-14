import time

from selenium import webdriver

import pygame

music_file = "1.mp3"

browser = webdriver.Chrome("C:/Users/ficd0/Desktop/새 폴더/chromedriver.exe")

browser.get('https://smartstore.naver.com/joytronstore/products/4652565090')
# browser.get('https://smartstore.naver.com/joytronstore/products/4872373481')

time.sleep(1)

tag_name = browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div[2]/form/fieldset/div[4]/div[2]/div[3]/span[1]')

a_tag = tag_name.find_element_by_tag_name('a')
if a_tag:
    print(a_tag)
    print('구매 가능')
elif tag_name.find_element_by_tag_name('span'):
    print('구매 불가')
else:
    print('오류')