from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.justdial.com/Bangalore/Event-Organisers/nct-10194150"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
page = requests.get(url, headers=headers)

print("Response Code : ", page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

event_planners = []

result_boxes = soup.find_all("div", {"class": "resultbox_info"})

try:
    for result_box in result_boxes:
        content = result_box.find("div", {"class": "resultbox_textbox"})

        # Extracting Title
        title = content.find("h2")
        link = title.find("a", {"class": "resultbox_title_anchor"})['href']

        # If link not starts with https://www.justdial.com, add it to the link
        if not link.startswith("https://www.justdial.com"):
            link = "https://www.justdial.com" + link

        name = title.find("a", {"class": "resultbox_title_anchor"}).text.strip()
        print(name)
        print(link)

        #Extracting Number
        number = content.find("span", {"class": "callNowAnchor"}).text
        print(number)
        print("---------------------------------------------------")

        # Creating a dictionary
        data = {
            "name": name,
            "link": link,
            "number": number
        }

        event_planners.append(data)
except:
    print("Script execution failed.")

# Writing to CSV
csv_file_path = "event_planners.csv"

existing_data = []
try:
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            existing_data.append(row)
except FileNotFoundError:
    existing_data = []


new_data = []
for entry in event_planners:
    if entry not in existing_data:
        new_data.append(entry)

# Append only the new data to the CSV file
with open(csv_file_path, 'a', newline='') as file:
    fieldnames = ["name","link", "number"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # If the file is empty, write the header row
    if not existing_data:
        writer.writeheader()

    # Write the new data to the file
    for entry in new_data:
        writer.writerow(entry)

print("New data has been successfully appended to the CSV file.")