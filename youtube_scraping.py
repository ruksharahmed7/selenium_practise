
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.common.by import By
import pandas as pd

data = pd.DataFrame({
    'title':[],
    'author':[],
    'views':[],
    'link':[],
})


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


driver.get("https://www.youtube.com/")
video_elems = driver.find_elements(By.TAG_NAME, 'ytd-rich-item-renderer' )
print(len(video_elems))
# titles = []
# for elem in video_elems:
#     try: 
#         title = elem.find_element(By.XPATH,".//a[@id='video-title-link']")
#         title_text = title.get_attribute('title')
#         print(title_text)
#         print('$$$$$$$$$$$$$$$')
#         titles.append(title_text)
#     except:
#         print('Could not find title')

for i in range(len(video_elems)):
    # we loop through every WebElement and print different attributes
    try:
        title = video_elems[i].find_element(By.XPATH, ".//a[@id='video-title-link']").text
    except:
        title = 'NULL'
    
    try:
        author = video_elems[i].find_element(By.XPATH, ".//a[@id='avatar-link']").get_attribute('title')
    except:
        author = 'NULL'
    
    try:
        views = video_elems[i].find_element(By.XPATH, ".//a[@id='video-title-link']").get_attribute('aria-label')
        # for views, we also need regex to extract it from aria-label
        views = re.search(r"(?i)[0-9,]+(?= view)", views).group(0).replace(',', '')
    except:
        views = 'NULL'
    
    try:
        link = video_elems[i].find_element(By.XPATH, ".//a[@id='video-title-link']").get_attribute('href')
    except:
        link = 'NULL'
    
    
    # add results
    data = data.append({
        'title': title,
        'author': author,
        'views': views,
        'link': link
    }, ignore_index=True)
    
    # delete data
    del title, author, views, link

data.to_csv('data.csv', index=False)