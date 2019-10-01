import urllib.request
import os 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from time import sleep
import insta_url

def get_img_url():
    temp = []
    myurl = insta_url.my_url_list()
    driver = webdriver.Chrome('chromedriver.exe')
    for i in myurl:
        url = 'https://www.instagram.com/'+str(i)
        driver.get(url)

        while(1):
            sleep(1)
            pageString = driver.page_source 
            soup = BeautifulSoup(pageString, "lxml")
            imgs = soup.select('img')[1]
            imgs = imgs.attrs['src']
            temp.append(imgs)
            try :
                driver.find_element_by_class_name("coreSpriteRightChevron").click()

            except NoSuchElementException :
                break

        
        
    
    driver.close()
    print('이미지 주소 수집완료')
    return temp
