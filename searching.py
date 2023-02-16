from bs4 import BeautifulSoup
import requests
import re

url = "https://niet.instituteoncloud.com/Dashboard/StudentDashboard"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# Print the input field
print(soup.find_all(["input"], type="text"))

# Find using regular expressions
print(soup.find_all(text=re.compile("login")))

# Find using text inside the element
print(soup.find_all(text="Secure login")[0].parent)