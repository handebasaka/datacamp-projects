# Import pandas library
import pandas as pd

# Read the data
nobel = pd.read_csv('./datasets/nobel.csv')

# Find the most commonly awarded gender and birth country
top_gender = nobel['sex'].value_counts().index[0]
print(top_gender)

top_country = nobel['birth_country'].value_counts().index[0]
print(top_country)

# Calculate the decade column
nobel['decade'] = (nobel['year'] - nobel['year'] % 10).astype(int)

# Find the decade had the highest proportion of US-born winners
nobel_usa = nobel[nobel['birth_country'] == 'United States of America']
max_decade_usa = nobel_usa['decade'].value_counts(normalize= True).index[0]
print(max_decade_usa)

# Calculate proportions of female laureates by decade and category pair
nobel['female_winners'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index= False)['female_winners'].mean()

# Find the highest proportion of decade and category pair and save in a dictionary
max_female_decade_category = prop_female_winners[prop_female_winners['female_winners'] == prop_female_winners['female_winners'].max()]
max_female_dict = {max_female_decade_category['decade'].values[0] : max_female_decade_category['category'].values[0]}
print(max_female_dict)

# Find the first woman to receive a Nobel Prize, and her category
nobel_woman = nobel[nobel['female_winners']]
first_woman = nobel_woman[nobel_woman['year'] == nobel_woman['year'].min()]

first_woman_name = first_woman['full_name'].values[0]
first_woman_category = first_woman['category'].values[0]
print(f"\n The first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")

# Find individuals or organizations have won multiple Nobel Prizes throughout the years and save them in a list
counts_nobel = nobel['full_name'].value_counts()
repeat_nobel = counts_nobel[counts_nobel > 1].index
repeat_list = list(repeat_nobel)

print('\n The repeat winners are :', repeat_list)