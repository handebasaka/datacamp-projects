# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
crimes = pd.read_csv('./datasets/crimes.csv', dtype={"TIME OCC": str})

# Take a glance at the data
# print(crimes.head(10))

# Add hour info (HH format) as an int
crimes['HOUR'] = crimes['TIME OCC'].str[:-2].astype(int)

# Find the hour has the highest frequency of crimes and store as an int variable
peak_crime_hour = crimes['HOUR'].value_counts(normalize= True).index[0]

print(f"The hour with the largest volume of crime is {peak_crime_hour}")

# Visualize the frequency of crimes by hour with a countplot
sns.countplot(data= crimes, x= 'HOUR')
plt.xlabel('Hour of crime')
plt.ylabel('Counts of crime')
plt.title('The Frequency of Crimes by Hour')
plt.show()

# Locate the area has the largest frequency of night crimes (between 10pm and 3:59am)
night_crimes = crimes[crimes['HOUR'].isin([22, 23, 0, 1, 2, 3])]
peak_night_crime_location = night_crimes['AREA NAME'].value_counts(normalize = True).index[0]

print(f"The area with the largest volume of night crime is {peak_night_crime_location}")

# Create bins and labels for victim age ranges
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

# Add a new column using pd.cut() to bin values into discrete intervals
crimes["Age Bracket"] = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels)

# Find the category with the largest frequency
victim_ages = crimes["Age Bracket"].value_counts()
print(victim_ages)