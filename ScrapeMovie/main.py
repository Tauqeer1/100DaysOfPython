from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

movie_title = soup.find_all('span', class_='content_content__i0P3p')
# for title in movie_title:
#     if title.find('h2') and title.find('h2').find('strong'):
#         title_text = title.find('h2').find('strong').get_text()
#         print(title_text)

title_text = [title.find('h2').find('strong').get_text()
              for title in movie_title
              if title.find('h2') and title.find('h2').find('strong')]








