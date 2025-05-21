from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/ishop/Documents/chromedriver/chromedriver"


 # Create a Service object
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_element = driver.find_element("id", "articlecount")
li_elements = article_element.find_elements("tag name", "li")
anchor_tag = li_elements[1].find_elements("tag name", "a")[0]
article_count = int(anchor_tag.text.replace(",", ""))
print(article_count)

new_article_element = driver.find_element(By.CSS_SELECTOR, "#articlecount li:nth-child(2) > a:first-child")
print(new_article_element.text)