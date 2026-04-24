import requests
from bs4 import BeautifulSoup

def scrape_craigslist():
    url = "https://portland.craigslist.org/search/cta?query=4x4+truck&min_auto_year=2003&max_auto_year=2015"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "lxml")

    listings = []

    for item in soup.select(".result-title"):
        listings.append({
            "title": item.text,
            "link": item.get("href")
        })

    return listings
