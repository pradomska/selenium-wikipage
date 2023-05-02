from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=webdriver.ChromeOptions())
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(article_count.text)

driver.quit()
