from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep


chromedriver="chromedriver"
driver=webdriver.Chrome(chromedriver)
#chromedriver additional options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.page_load_strategy = 'eager'

#start the automated gogole chrome
driver = webdriver.Chrome(chromedriver,options=options)
driver.get('http://v.baidu.com/top/')
sleep(10)

#Locate the tv show object in the page
section_video_list = driver.find_elements(By.XPATH,'//*[@id="tvplay-section"]/div[2]/ul/li')

title_list = []
actors_list = []
for i in range(len(section_video_list)):
    video_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="tvplay-section"]/div[2]/ul/li')))
    video_meta = video_list[i].find_element(By.TAG_NAME,'div')
    title = video_meta.find_element(By.TAG_NAME,'h3')
    anchor = title.find_element(By.TAG_NAME,'a')
    title_list.append(anchor.text) 
    #print(anchor.text)
    
    #redirect the detail page to get the actor list for this tv drama
    driver.get(anchor.get_attribute('href'))
    actor_list = driver.find_elements(By.XPATH,'//*[@id="tv-intro"]/div[3]/div/div[1]/div[4]/a')
    temp_list=[]
    for actor in actor_list:
        temp_list.append(actor.text.replace('/',''))
        #print(actor.text)
    actors_list.append(temp_list)
    driver.back()
    sleep(5)
    
driver.quit()

top_list_dict={'title':title_list,
               'actors':actors_list}
df = pd.DataFrame(top_list_dict)
print(df)

