import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = []
ratings = []
years = []

movie_containers = soup.find_all('td', class_='titleColumn')
rating_containers = soup.find_all('td', class_='ratingColumn imdbRating')

for container in movie_containers:
    title = container.find('a').text
    year = container.find('span', class_='secondaryInfo').text.strip('()')
    titles.append(title)
    years.append(year)

for container in rating_containers:
    rating = container.strong.text
    ratings.append(rating)

movies_df = pd.DataFrame({'title': titles, 'year': years, 'rating': ratings})
movies_df.to_csv('top_250_movies.csv', index=False)
