from bs4 import BeautifulSoup
import requests
import csv

url = "https://internshala.com/internships/work-from-home-internships/"
html = requests.get(url)

soup = BeautifulSoup(html.text, "html.parser")

total_pages = int(soup.find(id="total_pages").text)

internship_data = []

try:
    page_range = int(input(f"How many pages do you want to parse?: (max-{total_pages}): "))
except:
    page_range = total_pages


for page in range(1, page_range+1):
    url = f"https://internshala.com/internships/work-from-home-internships/page-{page}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

    internships = soup.find_all("div", class_="internship_meta")
    
    for internship in internships:
        c_details = internship.find("div", class_="company")
        profile = c_details.find(class_="profile").text.strip()
        company = c_details.find(class_="company_name").text.strip()

        internship_other_detail = internship.find("div", class_="internship_other_details_container")
        other_details = internship_other_detail.find_all("div", class_="other_detail_item")
        start_date = other_details[0].find("div", id="start-date-first").find_all("span")[-1].text
        duration = other_details[1].find("div", class_="item_body").text.strip()
        raw_stipend = other_details[2].find("span", class_="stipend").text.split("/")[0][1:]
        stipend = 0 if raw_stipend == "npaid" else raw_stipend

        internship_post = {
            "Profile": profile,
            "Company": company,
            "Stipend": stipend,
            "Start Date": start_date,
            "Duration": duration,
        }

        internship_data.append(internship_post)

    print(f"Parsed page {page}, Total Found: {len(internship_data)} posts")

print(f"PARSING COMPLETE, found {len(internship_data)} posts")

with open('./internshala.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Profile", "Company", "Stipend", "Start Date", "Duration"])

    for data in internship_data:
        writer.writerow([data["Profile"],
            data["Company"],
            data["Stipend"],
            data["Start Date"],
            data["Duration"]
        ])

print("Finished Parsing: Saved data to internshala.csv")