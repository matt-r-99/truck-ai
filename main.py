
from scraper import scrape_craigslist
from scorer import score_listing
import time

def run():
    listings = scrape_craigslist()

    results = []
    
    for listing in listings[:10]: #keep light for cloud limits
        result = score_listing(listing)

        results.append ({
            "title": listing["title"],
            "result": result
        })
        print(listing["title"])
        print(result)
        print ("---")

    return results

    if __name__ == "__main__":
        run()
        print("-----")

while True:
    run()
    time.sleep(21600)  # every 6 hours
