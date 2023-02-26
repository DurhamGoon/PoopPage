import requests
from bs4 import BeautifulSoup

twitter_poop_url = "https://twitter.com/search?q=poop&src=typed_query&f=live"

page = requests.get(twitter_poop_url)
soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())