from bs4 import BeautifulSoup
import requests

# Use any Snapdeal url to get price info
url = 'https://www.snapdeal.com/product/stay-healthy-silicone-heel-protector/682622706581'

result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="Rs.")
parent = prices[-1].parent.parent.parent.parent
price = parent.find("div", {"id": "mainPrduct"})

title = doc.find_all("h1")[0]
print(title.string.strip())

print(price.string)