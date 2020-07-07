from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame

chrome_path= "D:/Download/chromedriver_win32/chromedriver.exe"

music_file = "1.mp3"

cnt = 1


def browser_form(domain):
    global cnt
    globals()['browser'+str(cnt)] = webdriver.Chrome(chrome_path)
    globals()['browser'+str(cnt)].get(domain)
    cnt += 1

browser_form('http://www.tmon.co.kr/deal/1898373862?keyword=%EB%8B%8C%ED%85%90%EB%8F%84%EC%8A%A4%EC%9C%84%EC%B9%98&tl_area=SALDEAL&tl_ord=2&searchClick=DL%7CND%7CBM&thr=ma')


try:
    title = WebDriverWait(browser1,  3) \
    .until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/section[1]/section[1]/section[1]/div[3]/div[13]/div[1]/div/div[1]/div/div/div/div/div[1]/ul/li[1]')))
    title2 = browser1.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/section[1]/section[1]/section[1]/div[3]/div[13]/div[1]/div/div[1]/div/div/div/div/div[1]/ul/li[2]')

    sold_out = title.get_attribute('class')
    sold_out2 = title2.get_attribute('class')

    print(sold_out)
    print(sold_out2)

finally:
    browser1.quit()