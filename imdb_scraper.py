import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import sys


def get_movie_data(soup):
    movies = []
    table = soup.find("table", class_="chart")
    rows = table.find_all("tr")

    for row in rows[1:]:
        title_col = row.find("td", class_="titleColumn")
        title = title_col.a.text
        year = title_col.span.text.strip("()")
        rating_col = row.find("td", class_="ratingColumn imdbRating")
        rating = rating_col.strong.text if rating_col.strong else None

        movie_data = {"title": title, "year": year, "rating": rating}
        movies.append(movie_data)

    return movies


def save_to_csv(movies, file_name):
    keys = movies[0].keys()
    with open(file_name, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(movies)
    return file_name


def scrape_imdb_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    if "toptv" in url or "tvmeter" in url:
        file_name = "top_tv_shows.csv"
    else:
        file_name = "top_movies.csv"

    movies = get_movie_data(soup)
    return save_to_csv(movies, file_name)


if __name__ == "__main__":
    url = input("Enter the IMDb list URL: ")
    scrape_imdb_list(url)
