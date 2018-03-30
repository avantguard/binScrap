from BeautifulSoup import BeautifulSoup
import requests
from time import sleep

page = "https://support.binance.com/hc/en-us/sections/115000106672-New-Listings"
query = requests.get(page)
soup = BeautifulSoup(query.text)
results = soup.findAll("li", {"class": "article-list-item "})

print "==============================="
print " Newly Added Coins on Binance: "
print "==============================="
sleep(1)

for result in results:
    print result.text