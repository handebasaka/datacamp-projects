## Introduction to the 'Visualizing the History of Nobel Prize Winners'

The Nobel Prize has been among the most prestigious international awards since 1901. Each year, awards are bestowed in chemistry, literature, physics, physiology or medicine, economics, and peace. In addition to the honor, prestige, and substantial prize money, the recipient also gets a gold medal with an image of Alfred Nobel (1833 - 1896), who established the prize.

The Nobel Foundation has made a dataset available of all prize winners from the outset of the awards from 1901 to 2023. The dataset used in this project is from the Nobel Prize API and is available in the `nobel.csv` file.

In this project, we'll get a chance to explore and answer several questions related to this prizewinning data.

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `year` | int64 | Year of nobel prize |
| 1 | `category` | object | Category of prize |
| 2 | `prize` | object | Full name of nobel prize |
| 3 | `motivation` | object | Motivation of the study |
| 4 | `prize_share` | object | Share amount of the prize |
| 5 | `laureate_id` | int64 | The ID of winners |
| 6 | `laureate_type` | object | Types of winners |
| 7 | `full_name` | object | Full name of winners |
| 8 | `birth_date` | object | Birth date of winners |
| 9 | `birth_city` | object | Birth city of winners |
| 10 | `birth_country` | object | Birth country of winners |
| 11 | `sex` | object | Sex of winners |
| 12 | `organization_name` | object | Organization name of winners |
| 13 | `organization_city` | object | Organization city of winners |
| 14 | `organization_country` | object | Organization country of winners |
| 15 | `death_date` | object | Death date of winners |
| 16 | `death_city` | object | Death city of winners |
| 17 | `death_country` | object | Death country of winners |

## Goals
- What is the most commonly awarded gender and birth country? Storing the string answers as `top_gender` and `top_country`.
- What decade had the highest proportion of US-born winners? Store this as an integer called `max_decade_usa`.
- What decade and category pair had the highest proportion of female laureates? Store this as a dictionary called `max_female_dict` where the decade is the key and the category is the value.
- Who was the first woman to receive a Nobel Prize, and in what category? Save your string answers as `first_woman_name` and `first_woman_category`.
- Which individuals or organizations have won multiple Nobel Prizes throughout the years? Store the full names in a list named `repeat_list`.

## Tools and Technologies Used
`Python`

`Pandas` for data manipulation 

## How to Run
clone:
```sh
git clone https://github.com/handebasaka/datacamp-projects
```
open the solution file:
```bash
cd datacamp-projects/visualizing-the-history-of-nobel-prize-winners
```
run python script:
```bash
python3 solution.py
```
