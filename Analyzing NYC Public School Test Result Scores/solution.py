# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the data
schools = pd.read_csv("Analyzing NYC Public School Test Result Scores/datasets/schools.csv")

# Preview the data
schools.head()

# Create best_math_schools with at least 80% of the max score in math
pos_max_score = 800
best_math_schools = (schools[schools['average_math'] >= pos_max_score * 0.8])[['school_name', 'average_math']].sort_values('average_math', ascending = False)
print(best_math_schools)

# Create top_10_schools over total_SAT score
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name', 'total_SAT']].sort_values('total_SAT', ascending= False).head(10)
print(top_10_schools)

# Locate the borough with the largest std dev of total_SAT
borough_schools = schools.groupby('borough', as_index = True)['total_SAT'].agg(['count', 'mean', 'std']).round(2)

largest_std_dev = borough_schools[borough_schools['std'] == borough_schools['std'].max()]
largest_std_dev = largest_std_dev.rename(columns= {'count': 'num_schools', 'mean': 'average_SAT', 'std': 'std_SAT'})
print(largest_std_dev)

# Visualize a summary of SAT scores by boroughs
sns.catplot(x= 'borough', y= 'total_SAT', data= schools, hue= 'borough', kind= 'bar', ci= None)
plt.xticks(rotation=45)
plt.show()