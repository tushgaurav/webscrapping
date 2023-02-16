from bs4 import BeautifulSoup
import requests
import re

url = "https://www.coinmarketcap.com"
result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")

tbody = soup.tbody
trs = tbody.contents

# print(trs[0].next_sibling)
# print(trs[1].previous_sibling)
# print(list(trs[0].next_siblings))

crypto_prices = {}

for tr in trs:
    try:
        name = tr.find(class_="ePTNty").text
        price = tr.find(text=re.compile("\$")).text
        crypto_prices[name] = price
    except:
        pass

# print(crypto_prices)

for name in crypto_prices:
    price = crypto_prices[name]
    print(f"{name} is priced now at {price}")