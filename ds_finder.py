from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pygame

music_file = "1.mp3"   # mp3 or mid file
error_file = "2.mp3"   # mp3 or mid file

# Chrome_path 
chrome_path= "D:\Download\chromedriver_win32 (1)\chromedriver.exe"

cnt = 1

def alert(mfile):
    freq = 16000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
    bitsize = -16   # signed 16 bit. support 8,-8,16,-16
    channels = 1    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get right sound)

    # default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.load(mfile)
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    pygame.mixer.quit()    


def browser_form(domain):
    global cnt
    globals()['browser'+str(cnt)] = webdriver.Chrome(chrome_path)
    globals()['browser'+str(cnt)].get(domain)
    cnt += 1



def go(location, result):
    if result:
        print(location)
        alert(music_file)
    else:
        print('구매 불가 {}'.format(cnt-1))




while True:

    # 소프라노

    browser_form('https://sofrano.com/product/detail.html?product_no=831&cate_no=55&display_group=1')

    try:
        title = WebDriverWait(browser1, 3) \
        .until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[6]/div[4]/div/div[4]/div[1]/a[3]')))
        result = title.text
        if result == '품 절':
            go('', False)
        else:
            go('소프라노 ㄱㄱㄱ', True)
            break

    except:
        print('에러')
        alert(error_file)
    finally:
        browser1.quit()

    # 조이트론

    browser_form('https://smartstore.naver.com/joytronstore/category/0cdf08e497434eb4b46d4e039ef504d4?cp=1')
    try:
        title = WebDriverWait(browser2,  3) \
        .until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/form/div[3]/ul/li[2]/div[3]')))
    
        sold_out = title.text

        if sold_out=='일시품절':
            go('', False)
        else:
            go('조이 트론 ㄱㄱㄱㄱ', True)
            break
    except:
        print('에러')
        alert(error_file)
    finally:
        browser2.quit()

    # 엔엔마켓

    browser_form('http://www.nnmarket.co.kr/shop/shopbrand.html?type=M&xcode=025&mcode=001')

    try:
        title = WebDriverWait(browser3,  3) \
        .until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'item-list')))

        for item in title:
            name = item.find_element(By.CLASS_NAME, 'prd-brand').text
            if name == '[스위치] Nintendo Switch 동물의 숲 에디션 본체 + 모여봐요 동물의숲 + 게임 1종 선택' or '닌텐도 스위치 동물의숲 에디션+ 포켓몬스터 이브이 몬스터볼 SET' or name == 'Nintendo Switch 모여봐요 동물의 숲 에디션' or name == '[스위치]닌텐도 스위치 모여봐요 동물의 숲 에디션+모여봐요 동물의 숲 + 도라에몽 진구의 목장이야기':

                price = item.find_element(By.CLASS_NAME, 'prd-price').text
                if price != 'Sold Out':
                    go('엔엔마켓 ㄱㄱㄱㄱ', True)
                    break
        
        go('', False)

    except:
        print('에러')
        alert(error_file)

    finally:
        browser3.quit()

    #  cjmall (이브이)

    # browser_form('http://display.cjmall.com/p/item/64095564?channelCode=30001001')

    
    # try:
    #     title = WebDriverWait(browser4,  3) \
    #     .until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[4]/div/div[2]/div[1]/div[2]/div[2]/div[2]/a')))
        
    #     sold_out = title.text

    #     if sold_out == '매진':
    #         go('', False)
    #     else:
    #         go('예스24 인질셋 ㄱㄱㄱㄱ',True)
    #         break
    # except:
    #     print('에러')
    #     alert(error_file)            


    # finally:
    #     browser4.quit()

    # 티몬

    browser_form('http://www.tmon.co.kr/deal/1898373862?keyword=%EB%8B%8C%ED%85%90%EB%8F%84%EC%8A%A4%EC%9C%84%EC%B9%98&tl_area=SALDEAL&tl_ord=2&searchClick=DL%7CND%7CBM&thr=ma')

    try:
        title = WebDriverWait(browser4,  3) \
        .until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/section[1]/section[1]/section[1]/div[3]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/ul/li[1]')))
        title2 = browser4.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/section[1]/section[1]/section[1]/div[3]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/ul/li[2]')

        sold_out = title.get_attribute('class')
        sold_out2 = title2.get_attribute('class')

        if sold_out != 'soldout' or sold_out2 != 'soldout':
            go('티몬 ㄱㄱㄱㄱ', True)
            break
        else:
            go('', False)
    except:
        print('에러')
        alert(error_file)
    finally:
        browser4.quit()
    
    
    cnt = 1