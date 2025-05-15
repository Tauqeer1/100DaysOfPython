import requests
from bs4 import BeautifulSoup

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"

user_input_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

billboard_url = f"{BILLBOARD_BASE_URL}/{user_input_date}"


billboard_response = requests.get(billboard_url,
                                  headers={"User-Agent": "Chrome/136.0.0.0"})
billboard_response.raise_for_status()
billboard_html_content = billboard_response.text

soup = BeautifulSoup(billboard_html_content, "html.parser")

print(soup.prettify())