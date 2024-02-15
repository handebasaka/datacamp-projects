## Introduction to the 'Analyzing Crime in Los Angeles'

Los Angeles, California 😎. The City of Angels. Tinseltown. The Entertainment Capital of the World!

Known for its warm weather, palm trees, sprawling coastline, and Hollywood, along with producing some of the most iconic films and songs. However, as with any highly populated city, it isn't always glamorous and there can be a large volume of crime. That's where you can help!

You have been asked to support the Los Angeles Police Department (LAPD) by analyzing crime data to identify patterns in criminal behavior. They plan to use your insights to allocate resources effectively to tackle various crimes in different areas.

The dataset is available in the `crimes.csv` file. It is a modified version of the original data, which is publicly available from Los Angeles Open Data.

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `DR_NO` | int64 | Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits |
| 1 | `Date Rptd` | datetime64[ns] | Date reported - MM/DD/YYYY |
| 2 | `DATE OCC` | datetime64[ns] | Date of occurrence - MM/DD/YYYY |
| 3 | `TIME OCC` | object | In 24-hour military time |
| 4 | `AREA NAME` | object | The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles. |
| 5 | `Crm Cd Desc` | object | Indicates the crime committed |
| 6 | `Vict Age` | int64 | Victim's age in years |
| 7 | `Vict Sex` | object | Victim's sex: `F`: Female, `M`: Male, `X`: Unknown |
| 8 | `Vict Descent` | object | Victim's descent: `A` - Other Asian `B` - Black `C` - Chinese `D` - Cambodian `F` - Filipino `G` - Guamanian `H` - Hispanic/Latin/Mexican `I` - American Indian/Alaskan Native `J` - Japanese `K` - Korean `L` - Laotian `O` - Other `P` - Pacific Islander `S` - Samoan `U` - Hawaiian `V` - Vietnamese `W` - White `X` - Unknown `Z` - Asian Indian |
| 9 | `Weapon Desc` | object | Description of the weapon used (if applicable) |
| 10 | `Status Desc` | object | Crime status |
| 11 | `LOCATION` | object | Street address of the crime |


## Goals
- Which hour has the highest frequency of crimes? Store as an integer variable called `peak_crime_hour`.
- Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? Save as a string variable called `peak_night_crime_location`.
- Identify the number of crimes committed against victims by age group (0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+). Save as a pandas Series called `victim_ages`.

## Tools and Technologies Used
`Python`

`Pandas` and `Numpy` for data manipulation

`Matplotlib` and `Seaborn` for data visualization

## How to Run
clone:
```sh
git clone https://github.com/handebasaka/datacamp-projects
```
open the solution file:
```bash
cd datacamp-projects/analyzing-crime-in-los-angeles
```
run python script:
```bash
python3 solution.py
```
