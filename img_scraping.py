# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

def removeimg():
    basePath="/Users/owner/Desktop/TEMP_FILE/img"
    for files in os.walk(".\img",topdown=False):
        for filename in files[2]:            
# deleting the images with jpeg format and size is less than 5KB
            if filename.endswith(".jpg") and os.path.getsize(files[0]+'\\'+filename)<5120:
                print("Removing item "+files[0]+'\\'+filename)
                os.remove(files[0]+'\\'+filename)

def getbaiduimage(keyword,dir_name):
    chromedriver="chromedriver"
    driver = webdriver.Chrome(chromedriver)
    baseURL = "https://image.baidu.com"
    driver.get(baseURL)
    sleep(3)
    #input text into search box
    sbox = driver.find_element_by_xpath('//*[@id="kw"]')
    sbox.send_keys(keyword.encode('utf-8').decode('utf-8'))
    btn = driver.find_element_by_class_name('s_search')
    btn.click()
    sleep(3)
    #locate image box in the page
    div_img=driver.find_elements_by_class_name('imgbox')
    download_link = div_img[0].find_element_by_tag_name('a')
    driver.get(download_link.get_attribute('href'))
    sleep(3)
    if not os.path.exists('img/'+dir_name):
        os.mkdir('img/'+dir_name)
    else:
        print("The directory is already exist")
    #keep iteration for retrieve the image n times
    for keep in range(1,30):
        curr_img = driver.find_element_by_xpath('//*[@id="currentImg"]')
        #image = download_link.find_element_by_tag_name('img')
        path = curr_img.get_attribute('src')
        print(path)
        urlretrieve(path,"/Users/owner/Desktop/TEMP_FILE/img/"+dir_name+'/'+str(keep)+".jpg")
        driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
        sleep(1)
    print("Download Complete!")
    driver.close()
#end of function

getbaiduimage("赵丽颖","zly")
removeimg()
