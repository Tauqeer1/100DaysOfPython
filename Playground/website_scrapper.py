from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

all_articles_tag = soup.find_all(class_='titleline')
score_tag = soup.find_all(name='span', class_='score')
article_texts = []
article_links = []
for article_tag in all_articles_tag:
    anchor_tag = article_tag.find('a')
    article_texts.append(anchor_tag.get_text())
    article_links.append(anchor_tag.get('href'))

article_upvotes = [int((score.get_text()).split()[0]) for score in score_tag]
print(article_texts)
print(article_links)
print(article_upvotes)

highest_vote = max(article_upvotes)
highest_vote_index = article_upvotes.index(highest_vote)

article = article_texts[highest_vote_index]
link = article_links[highest_vote_index]
print(article)
print(link)

