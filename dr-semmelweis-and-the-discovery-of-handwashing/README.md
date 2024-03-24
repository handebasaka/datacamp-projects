## Introduction to the 'Dr. Semmelweis and the Discovery of Handwashing'

Dr. Ignaz Semmelweis, a Hungarian physician born in 1818 and active at the Vienna General Hospital. He's thinking about childbed fever: A deadly disease affecting women that just have given birth. He is thinking about it because in the early 1840s at the Vienna General Hospital as many as 10% of the women giving birth die from it. He is thinking about it because he knows the cause of childbed fever: It's the contaminated hands of the doctors delivering the babies. And they won't listen to him and wash their hands!

In this project, we'll analyze the data of Semmelweis's discovery of handwashing and figure out whether it is True or False that doctors should wash their hands.

The dataset is available in the `yearly_deaths_by_clinic.csv` file. It contains the number of women giving birth at the two clinics at the Vienna General Hospital for the years 1841 to 1846.

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `year` | int64 | Year |
| 1 | `births` | int64 | Number of births |
| 2 | `deaths` | int64 | Number of deaths |
| 3 | `clinic` | object | Name of clinics |

Semmelweis saw the proportion of deaths consistently so much higher in Clinic 1. The only difference between the clinics was that many medical students served at Clinic 1, while mostly midwife students served at Clinic 2. While the midwives only tended to the women giving birth, the medical students also spent time in the autopsy rooms examining corpses.

Semmelweis started to suspect that something on the corpses spread from the hands of the medical students, caused childbed fever. So in a desperate attempt to stop the high mortality rates, he decreed: Wash your hands! This was an unorthodox and controversial request, nobody in Vienna knew about bacteria at this point in time.

The second dataset is available in the `monthly_deaths.csv` file. It contains the montly number of women giving birth from Clinic 1.

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `date` | datetime64 | Date |
| 1 | `births` | int64 | Number of births |
| 2 | `deaths` | int64 | Number of deaths |


## Goals
- Load in the dataset with the yearly number of deaths as `yearly`.
- Calculate the proportion of deaths per number of births and store the result in a new column named `proportion_deaths`. Extract the rows from Clinic 1 into `clinic_1` and the rows from Clinic 2 into `clinic_2`.
- Plot the yearly proportion of deaths for both clinics in a single plot. Label the plotted lines using the `label` argument to `.plot()`. Change the y-axis label to "Proportion deaths" using the `ylabel` parameter in your second call of `.plot()`. Save the Axes object returned by the `plot` method into the variable `ax`.
- Load in the dataset with the monthly number of deaths for Clinic 1 as `monthly`. Make sure to tell `read_csv` to parse the `date` column as a date. Calculate the proportion of `deaths` per number of `births` and store the result in the new column `proportion_deaths`. Print out the first rows in `monthly` using the `.head()` method.
- Plot the monthly proportion of deaths by `date` for Clinic 1. Change the y-axis label to "Proportion deaths". Save the Axes object returned by the `.plot()` method into the variable `ax`.
- Make a plot that highlights the effect of handwashing (when Semmelweis made handwashing obligatory). Save the date `1847-06-01` as `handwashing_start`. Split `monthly` into `before_washing` (the rows in monthly before handwashing_start) and `after_washing` (the rows in monthly at and after handwashing_start). Using the same approach you used in Task 3, plot `proportion_deaths` in `before_washing` and `after_washing` into the same plot. Again, use the DataFrame `.plot()` method twice, saving the Axes object returned by the first call of `.plot()` into the variable `ax`. Label the plotted lines using the `label` argument to `.plot()`. Change the y-axis label to "Proportion deaths" in your second call of `.plot()`.
- Calculate the average reduction in proportion of deaths due to handwashing. Select the column `proportion_deaths` in `before_washing` and assign it to `before_proportion`. Do the same for `proportion_deaths` in `after_washing` and assign it to `after_proportion`. Calculate the difference in mean monthly proportion of deaths as mean `after_proportion` minus mean `before_proportion`.
- Make a bootstrap analysis of the difference in mean monthly proportion of deaths.
    - Within your `for` loop:
        - `boot_before` and `boot_after` should be sampled with replacement from `before_proportion` and `after_proportion`.
        - The difference in means should be appended to `boot_mean_diff`.
    - Calculate a 95% `confidence_interval` as the 2.5% and 97.5% quantiles of `boot_mean_diff`.
- Given the data Semmelweis collected, is it True or False that doctors should wash their hands?

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
cd datacamp-projects/dr-semmelweis-and-the-discovery-of-handwashing
```
run python script:
```bash
python3 solution.py
```
