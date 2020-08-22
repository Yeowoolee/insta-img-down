from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium import webdriver
import urllib.parse
from urllib.request import Request, urlopen
from time import sleep


def my_url_list(driver):
    search = input("주소를 입력하세요 : " )
    limit = int(input("수집 게시글 limit(0입력 = limit없음) : " ))

    url = str(search)
    #driver = webdriver.Chrome('chromedriver.exe')

    driver.get(url) 
    sleep(5)


    SCROLL_PAUSE_TIME = 1.0
    reallink = []

    while True:
        pageString = driver.page_source
        bsObj = BeautifulSoup(pageString, "lxml")
        
        for link1 in bsObj.find_all(name="div",attrs={"class":"Nnq7C weEfm"}):
                title = link1.select('a')[0] 
                if title:
                    real = title.attrs['href']
                    reallink.append(real)

                if limit != 0 and limit == len(reallink):
                    stop = True
                    break
                
                title = link1.select('a')[1]
                if title: 
                    real = title.attrs['href']
                    reallink.append(real) 

                if limit != 0 and limit == len(reallink):
                    stop = True
                    break

                title = link1.select('a')[2] 
                if title:
                    real = title.attrs['href']
                    reallink.append(real)
                
                if limit != 0 and limit == len(reallink):
                    stop = True
                    break
        if stop == True:
            break

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

    reallink = list(set(reallink))
    reallinknum = len(reallink)
    print("총"+str(reallinknum)+"개의 URL 수집")
    return reallink

