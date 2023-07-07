
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


driver.get("https://www.google.co.uk/")

# search = driver.find_element(by=By.NAME,value="q")

# search.send_keys("Selenium")

# search.send_keys(Keys.ENTER)

# driver.save_screenshot('article.png')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys("John Doe") # enter your name in the search box
    search_box.submit() # submit the search
    results = driver.find_element(By.XPATH, "//div[@id='result-stats']")
    # for result in results:
    #     text = result.text.split()[1] # extract the number of results
    #     print(text)
    # save it to a file
    print(results.text)
    # with open("results.txt", "w") as f:
    #     f.write(text)
except Exception as e:
    print(f"An error occurred: {e}")


