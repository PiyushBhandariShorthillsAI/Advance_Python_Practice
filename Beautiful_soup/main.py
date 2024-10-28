# main_scraper.py
import requests
from bs4 import BeautifulSoup
from config import BASE_URL
from utils import clean_text
from storage import save_to_csv

def scrape():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, "lxml")

    articles = []
    for item in soup.select(".titleline > a"):
        title = clean_text(item.text)
        link = item["href"]
        articles.append((title, link))

    save_to_csv(articles)

if __name__ == "__main__":
    scrape()
