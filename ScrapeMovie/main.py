from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

movies_page = response.text

soup = BeautifulSoup(movies_page, 'html.parser')
print(soup.prettify())