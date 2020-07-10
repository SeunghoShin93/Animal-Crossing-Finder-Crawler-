from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame

chrome_path= "D:\Download\chromedriver_win32 (1)\chromedriver.exe"

music_file = "1.mp3"

cnt = 1


def browser_form(domain):
    global cnt
    globals()['browser'+str(cnt)] = webdriver.Chrome(chrome_path)
    globals()['browser'+str(cnt)].get(domain)
    cnt += 1

browser_form('https://sofrano.com/product/detail.html?product_no=831&cate_no=55&display_group=1')


try:
    title = WebDriverWait(browser1,  3) \
    .until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[6]/div[4]/div/div[4]/div[1]/a[3]')))
    # title2 = browser1.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/section[1]/section[1]/section[1]/div[3]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/ul/li[2]')

    sold_out = title.text
    # sold_out2 = title2.get_attribute('class')

    print(sold_out)
    # print(sold_out2)

finally:
    browser1.quit()