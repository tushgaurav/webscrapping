from bs4 import BeautifulSoup
import requests
import re

search = input("Enter the search term: ")

url = f"https://www.newegg.ca/p/pl?d={search}"
html = requests.get(url)

soup = BeautifulSoup(html.text, "html.parser")
print(soup.text)

pages = soup.find_all("strong")
print(pages)