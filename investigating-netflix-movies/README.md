## Introduction to the 'Investigating Netflix Movies'

Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.

Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV file containing Netflix data. They believe that the average duration of movies has been declining. Using your friends initial research, you'll delve into the Netflix data to see if you can determine whether movie lengths are actually getting shorter and explain some of the contributing factors, if any.

The data has been provided with a dataset called `netflix_data.csv`. Your friend suspects that movies are getting shorter and they've found some initial evidence of this. Having peaked your interest, you will perform exploratory data analysis on the data to understand what may be contributing to movies getting shorter over time.

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `show_id` | object | The ID of the show |
| 1 | `type` | object | Type of show |
| 2 | `title` | object | Title of the show |
| 3 | `director` | object | Director of the show |
| 4 | `cast` | object | Cast of the show |
| 5 | `country` | object | Country of origin |
| 6 | `date_added` | object | Date added to Netflix |
| 7 | `release_year` | int64 | Year of Netflix release |
| 8 | `duration` | int64 | Duration of the show in minutes |
| 9 | `description` | object | Description of the show |
| 10 | `genre` | object | Show genre |

## Goals
- Filter the data to remove TV shows and store as `netflix_subset`.
- Investigate the Netflix movie data, keeping only the columns "`title`", "`country`", "`genre`", "`release_year`", "`duration`", and saving this into a new DataFrame called `netflix_movies`.
- Filter `netflix_movies` to find the movies that are strictly shorter than 60 minutes, saving the resulting DataFrame as `short_movies`; inspect the result to find possible contributing factors.
- Using a for loop and if/elif statements, iterate through the rows of `netflix_movies` and assign colors of your choice to four genre groups ("Children", "Documentaries", "Stand-Up", and "Other" for everything else). Save the results in a `colors` list. Initialize a matplotlib figure object called fig and create a scatter plot for movie duration by release year using the colors list to color the points and using the labels "`Release year`" for the x-axis, "`Duration (min)`" for the y-axis, and the title "`Movie Duration by Year of Release`".
- After inspecting the plot, answer the question "Are we certain that movies are getting shorter?" by assigning either "yes" or "no" to the variable `answer`.

## Tools and Technologies Used
`Python`

`Pandas` for data manipulation 

`Matplotlib` for data visualization

## How to Run
clone:
```sh
git clone https://github.com/handebasaka/datacamp-projects
```
open the solution file:
```bash
cd datacamp-projects/investigating-netflix-movies
```
run python script:
```bash
python3 solution.py
```
