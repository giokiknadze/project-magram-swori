import requests
import csv
from bs4 import BeautifulSoup

columns = ['number', 'name', 'year', 'platform', 'score', 'votes']

with open('main.csv', 'a', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(columns)

url = 'https://steam250.com/top250'
response = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
soup = BeautifulSoup(response.text, 'html.parser')
games = soup.find_all('div', class_="appline")

for number, game in enumerate(games, start=1):
    name = game.find('span', class_="title")
    year = game.find('span', class_="date")
    score = game.find('span', class_="score")
    votes = game.find('span', class_="votes")
    platform = game.find('span', class_="platforms")

    # Check if elements exist before accessing attributes or text
    name_text = name.text if name else ''
    year_text = year.text if year else ''
    score_text = score.text if score else ''
    votes_text = votes.text if votes else ''
    platform_text = platform.text if platform else ''

    with open('game.csv', 'a', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([number, name_text, year_text, platform_text, score_text, votes_text])

print(f"Done writing {len(games)} entries to game.csv")
