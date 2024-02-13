# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
netflix_df = pd.read_csv('./datasets/netflix_data.csv')

# Preview the data
netflix_df.head()

# Filter and store only movies
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Filter movies with necessary columns
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Find the movies that are strictly shorter than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]

# Create colors list for genres
colors = []

for label, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append('yellow')
    elif row['genre'] == 'Documentaries':
        colors.append('red')
    elif row['genre'] == 'Stand-Up':
        colors.append('blue')
    else:
        colors.append('gray')


# Create a scatter plot for movie duration by release year using the colors list to color the points
fig = plt.figure(figsize=(12, 8))
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c= colors, alpha= 0.75)

plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.show()

# Are we certain that movies are getting shorter?
answer = 'no'