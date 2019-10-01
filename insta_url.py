from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium import webdriver
import urllib.parse
from urllib.request import Request, urlopen
from time import sleep


def my_url_list():
    search = input("주소를 입력하세요 : " )
    url = str(search)
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get(url) 
    sleep(5)


    SCROLL_PAUSE_TIME = 1.0
    reallink = []

    while True:
        pageString = driver.page_source
        bsObj = BeautifulSoup(pageString, "lxml")

        for link1 in bsObj.find_all(name="div",attrs={"class":"Nnq7C weEfm"}):
            title = link1.select('a')[0] 
            real = title.attrs['href']
            reallink.append(real) 
            title = link1.select('a')[1] 
            real = title.attrs['href']
            reallink.append(real) 
            title = link1.select('a')[2] 
            real = title.attrs['href']
            reallink.append(real) 

        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
                
            else:
                last_height = new_height
                continue

    reallinknum = len(reallink)
    print("총"+str(reallinknum)+"개의 URL 수집")
    return reallink

