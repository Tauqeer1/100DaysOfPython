import requests
from bs4 import BeautifulSoup

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"

# user_input_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

# billboard_url = f"{BILLBOARD_BASE_URL}/{user_input_date}"
billboard_url = f"{BILLBOARD_BASE_URL}/1992-12-22"


billboard_response = requests.get(billboard_url,
                                  headers={"User-Agent": "Chrome/136.0.0.0"})
billboard_response.raise_for_status()
billboard_html_content = billboard_response.text

soup = BeautifulSoup(billboard_html_content, "html.parser")

h3_tags = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")

song_title = [h3_tag.get_text().strip() for h3_tag in h3_tags]
print(song_title)
