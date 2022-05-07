# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import datetime
import requests


def downloadPic():

    word = input("Input key word: ")
    url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ie=utf-8&word='+word+'&ct=201326592'
    result = requests.get(url)
    print(result.text)
    pic_url = re.findall('"objURL":"(.*?)",',result.text,re.S)
    i = 0
    print ('找到關鍵字:'+word+'的圖片，现在開始下載圖片...')
    for each in pic_url:
        print ('正在下載第'+str(i+1)+'張圖片，圖片地址:'+str(each))
        try:
            pic= requests.get(each, timeout=20)
        except requests.exceptions.ConnectionError:
            print ('【錯誤】當前圖片無法下載')
            
            continue

        current = "img/wwyx/"
        if not os.path.exists(current):
            os.mkdir(current)
        filename = word+'_'+str(i) + '.jpg'
 
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(current+filename,'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
    
def removeimg():
    basePath="/Users/ERIC_KWOK/Desktop/TEMP_FILE/img"
    for files in os.walk(".\img"):
        for filename in files[2]:            
            # deleting the images with jpeg format and size is less than 5KB
            if filename.endswith(".jpg") and os.path.getsize(files[0]+'\\'+filename)<5120:
                print("Removing item "+files[0]+'\\'+filename)
                os.remove(files[0]+'\\'+filename)

def change_filename(path='./img'):
    for f in os.walk(path):
        dirs_ls=f[1]
        break
    
    for d in dirs_ls:
        for root,dirs,files in os.walk(path+'/'+d):
            for filename in files:
                filepath = root+'/'+filename
                m_time = os.path.getmtime(filepath)
                m_date = datetime.datetime.fromtimestamp(m_time).strftime("%Y%m%d")
                m_datetime = datetime.datetime.fromtimestamp(m_time).strftime("%Y%m%d_%H%M%S")
                new_filename = path+'/'+d+'/'+m_date+'/'+m_datetime+".jpg"
                if not os.path.exists(path+'/'+d+'/'+m_date):
                    os.mkdir(path+'/'+d+'/'+m_date)
                else:
                    try:
                        os.rename(filepath,new_filename)
                        print(filename,"->",new_filename)
                    except:
                        continue
	
def getImage(url):
    chromedriver="chromedriver"
    driver=webdriver.Chrome(chromedriver)
    driver.get(url)
    sleep(5)
    today=datetime.date.today()
    if not os.path.exists('img/'+str(today)):
        os.mkdir('img/'+str(today))
        

    for page in range(1,11):
        print("page "+str(page))
        i=1
        a=driver.find_elements_by_class_name('anchor-card')
        
        for anchor in a:        
            img =anchor.find_element_by_tag_name('img')
            path= img.get_attribute("src")
            filename = str(page)+'_'+str(i)+".jpg"
            print(filename,path)
            urllib.request.urlretrieve(path,"/Users/ERIC_KWOK/Desktop/TEMP_FILE/img/"+str(today)+"/"+filename)
            i=i+1
        nextbtn = driver.find_element_by_xpath('//*[@id="ice_container"]/div/div/div[2]/div/div[1]/div[4]/div/div/div[2]/div/div/button[2]')  
        nextbtn.click()
        sleep(5)
    print("Download Completed!")
    driver.close()
    

def getbaiduimage(keyword,dir_name):
    chromedriver="chromedriver"
    #chromedriver additional options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    #start the chrome webdriver
    driver = webdriver.Chrome(chromedriver,options=options)
    baseURL = "https://image.baidu.com"
    driver.get(baseURL)
    sleep(2)
    
    #input text into search box
    sbox = driver.find_element(By.XPATH,'//*[@id="kw"]')
    sbox.send_keys(keyword.encode('utf-8').decode('utf-8'))
    btn = driver.find_element(By.CLASS_NAME,'s_newBtn')
    btn.click()
    sleep(2)
    
    #locate image box in the page
    div_img=driver.find_elements(By.CLASS_NAME,'imgbox')
    download_link = div_img[0].find_element(By.TAG_NAME,'a')
    driver.get(download_link.get_attribute('href'))
    sleep(3)
    if not os.path.exists('img/'+dir_name):
        os.mkdir('img/'+dir_name)
    else:
        print("The directory is already exist")
        
    #keep iteration for retrieve the image n times
    for keep in range(1,40):
        curr_img = driver.find_element(By.XPATH,'//*[@id="currentImg"]')
        path = curr_img.get_attribute('src')
        print(path)
        try:
            urllib.request.urlretrieve(path,"./img/"+dir_name+'/'+dir_name+'_'+str(keep)+".jpg")
        except Exception as e:
            print("Cannot download "+path+",Error:"+e)
            continue
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_RIGHT)
        sleep(0.1)
    print("Download Complete!")
    driver.quit()
#end of function
     
#getImage("https://v.taobao.com/v/content/live?catetype=704")
#removeimg()
change_filename()
#first parameter stand for the keyword of search box
#second parmeter stand for the name of directory
#getbaiduimage("杨幂","ym")
#getbaiduimage("迪丽热巴","dlrb")
#getbaiduimage("唐嫣","ty")
#getbaiduimage("赵丽颖","zly")
#downloadPic()
