from imdb_scraper import scrape_imdb_list
import pandas as pd

url = input("Enter the IMDb list URL: ")
output_file = scrape_imdb_list(url)

movies_df = pd.read_csv(output_file)

# Calculate the average rating
average_rating = movies_df["rating"].astype(float).mean()
print(f"Average rating of the top movies: {average_rating:.2f}")

# Calculate the number of movies per decade
movies_df["year"] = movies_df["year"].astype(int)
movies_df["decade"] = movies_df["year"] // 10 * 10
movies_per_decade = movies_df["decade"].value_counts().sort_index()
print("Number of movies per decade:")
print(movies_per_decade)
