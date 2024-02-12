## Introduction to the Data

Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a maximum score of 800 points. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.

Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend.

The data has been provided with a dataset called `schools.csv`. We will try to answer three key questions about New York City (NYC) public school SAT performance.

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `school_name` | object | Name of the school |
| 1 | `borough` | object | Borough where the school is located |
| 2 | `building_code` | object | Code representing the school building |
| 3 | `average_math` | int64 | Average math score for the SATs |
| 4 | `average_reading` | int64 | Average reading score for the SATs |
| 5 | `average_writing` | int64 | Average writing score for the SATs |
| 6 | `percent_tested` | float64 | Percentage of students who completed the SATs |

## Goals
- Create a pandas DataFrame called `best_math_schools` containing the "`school_name`" and "`average_math`" score for all schools where the results are at least 80% of the maximum possible score, sorted by "`average_math`" in descending order.
- Identify the top 10 performing schools based on scores across the three SAT sections, storing as a pandas DataFrame called `top_10_schools` containing the school name and a column named "`total_SAT`", with results sorted by `total_SAT` in descending order.
- Locate the NYC borough with the largest standard deviation for "`total_SAT`", storing as a DataFrame called `largest_std_dev` with "`borough`" as the index and three columns: "`num_schools`" for the number of schools in the borough, "`average_SAT`" for the mean of "`total_SAT`", and "`std_SAT`" for the standard deviation of "`total_SAT`". Round all numeric values to two decimal places.

## Tools and Technologies Used
`Python`

`Pandas` for data manipulation 

`Matplotlib` and `Seaborn` for data visualization

## Learn More
### Documentation
- [Pandas user guide & API references](https://pandas.pydata.org/docs/index.html)
- [Matplotlib user guide & tutorials](https://matplotlib.org/stable/)
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html)