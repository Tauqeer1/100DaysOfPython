from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/ishop/Documents/chromedriver/chromedriver"

# Create a Service object
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_widget = driver.find_element(By.CLASS_NAME, "event-widget")
ul_elements =  event_widget.find_elements(By.TAG_NAME, "ul")
event_dict = {}
for ul in ul_elements:
    li_items = ul.find_elements(By.TAG_NAME, "li")
    for index, li in enumerate(li_items):
        data = li.text.split("\n")
        event_dict[index] = {"time": data[0], "name": data[1]}

print(event_dict)



# driver.quit()
