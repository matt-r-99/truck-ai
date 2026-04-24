
from scraper import scrape_craigslist
from scorer import score_listing
import time

def run():
    listings = scrape_craigslist()

    for listing in listings[:5]:
        result = score_listing(listing)
        print(listing["title"])
        print(result)
        print("-----")

while True:
    run()
    time.sleep(21600)  # every 6 hours