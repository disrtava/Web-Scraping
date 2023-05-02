from bs4 import BeautifulSoup
import requests
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

headers = ['name','distance','mass','radius']
star_data = []

page_source = requests.get(url,verify = False)
soup = BeautifulSoup(page_source.content,'html.parser')

collected_data = soup.find('table')

for row in collected_data.find_all('tr'):
    td = row.find_all('td')
    td = [col.text.strip() for col in td]
    star_data.append(td)


star_data = star_data[1:]

with open("stars.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(star_data)