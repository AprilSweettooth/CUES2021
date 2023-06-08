import csv
from bs4 import BeautifulSoup
import requests
page = requests.get("https://olympics.com/en/olympic-games/tokyo-2020/medals")
soup = BeautifulSoup(page.content, 'html.parser')
country = soup.find_all(
    'span', class_="styles__CountryName-sc-fehzzg-6 kFXANP")
medal = soup.find_all(
    'span', class_="Medalstyles__Medal-sc-1tu6huk-1 ghnLFg")
print(country[92].get_text())
print(medal[92].get_text())

with open('rank.csv', mode='w') as rank_file:
    rank_writer = csv.writer(rank_file, delimiter=',',
                             quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(93):
        rank_writer.writerow(
            [str(country[i].get_text()), str(medal[i].get_text())])
