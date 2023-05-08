from get_movies import *

movies_df = pd.read_csv("top_250_movies.csv")

# Calculate the average rating
average_rating = movies_df["rating"].astype(float).mean()
print(f"Average rating of the top 250 movies: {average_rating:.2f}")

# Calculate the number of movies per decade
movies_df["decade"] = movies_df["year"] // 10 * 10
movies_per_decade = movies_df["decade"].value_counts().sort_index()
print("Number of movies per decade:")
print(movies_per_decade)
