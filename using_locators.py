
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


driver.get("https://www.browserstack.com/guide/how-ai-in-visual-testing-is-evolving")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

header=driver.find_element(By.ID, "toc0")

print(header.text)

