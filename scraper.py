
import requests
from bs4 import BeautifulSoup

def scrape_craigslist():
    url = "https://portland.craigslist.org/search/cto?query=4x4+truck"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    listings = []

    for item in soup.select(".result-title"):
        listings.append({
            "title": item.text,
            "link": item["href"]
        })

    return listings