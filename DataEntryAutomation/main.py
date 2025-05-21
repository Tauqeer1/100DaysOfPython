from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/ishop/Documents/chromedriver/chromedriver"

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeJhe0Hu9TZcdQ9WGoHXl_W14p_UN2zxr7CFCjX5Lnn0aIx9A/viewform?usp=header"
ZILLOW_URL = "https://www.zillow.com/homes/20330_rid/"


 # Create a Service object
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get(ZILLOW_URL)

grid_search_result_div = driver.find_element("id", "grid-search-results")
print(grid_search_result_div.text)

grid_search_result_div1 = driver.find_elements(By.CSS_SELECTOR, "#grid-search-results ul li")
for div in grid_search_result_div1:
    print(div.text)
