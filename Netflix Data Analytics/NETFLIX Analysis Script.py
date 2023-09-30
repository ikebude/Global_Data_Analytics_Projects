#Working on Real Project With Python
#The NetFlix Dataset
import pandas as pd
Netflix = pd.read_csv(r"C:\Users\user\Projects\Data-Analysis-Projects\Netflix Data Analytics\Netflix-Dataset.csv")
Netflix
#How to Analyze DataFrames
Netflix.head() # for the head of the data
Netflix.shape # for the total number of Rows and Columns
Netflix.index # for the Range of the Data
Netflix.columns # for the names of the Columns
Netflix.dtypes #this show the Kind of data a particular column is
Netflix.nunique() #shows the number of unique values in a table column
# Lets see the Basic information about the Data
Netflix.info()
# Lets look at the Data to see the number of null values in each column
Netflix.isnull().sum()
########################################################################################################
# Lets run some Analysis to view somw certain Updates
# Firstly we would want to see the heatmap of the null values
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(Netflix.isnull())
plt.show()
# For the Questions Part
### Task.1. Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.
Netflix[Netflix.duplicated()]
Netflix.drop_duplicates(inplace = True)
### Task.2. Is there any Null Value present in any column ? Show with Heat-map.
Netflix.isnull().sum()
sns.heatmap(Netflix.isnull())
plt.show()
### Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show?
Netflix[Netflix.Title == 'House of Cards']
#OR
Netflix[Netflix['Title'].isin(['House of Cards'])]       #  To show all records of a particular item in any column
#OR
Netflix[Netflix['Title'].str.contains('House of Cards')]          #  To show all records of a particular string in any column
### Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.
Netflix['Release_Date'] = pd.to_datetime(Netflix['Release_Date'])
Netflix.dtypes
Netflix['Year'] = Netflix.Release_Date.dt.year
# Value Counts
Netflix.Year.value_counts()
Netflix.Year.value_counts().plot(kind = 'bar')
### Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
Netflix['Category'].value_counts()
sns.countplot(Netflix['Category'])
### Q.4. Show all the Movies that were released in year 2020.
Netflix[(Netflix.Category == 'Movie') & (Netflix.Year == 2020)]
### Q.5. Show only the Titles of all TV Shows that were released in India only.
Netflix[(Netflix.Category == 'TV Show') & (Netflix.Country == 'India')] ['Title']
### Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
Netflix.Director.value_counts().head(10)
#### Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
Netflix[(Netflix.Category == 'Movie') & (Netflix.Type.str.contains('Comedies')) | (Netflix.Country == 'United Kingdom')]
Netflix[(Netflix.Category == 'Movie') & (Netflix.Type == 'Comedies') | (Netflix.Country == 'United Kingdom')]
### Q.8. In how many movies/shows, Tom Cruise was cast?
Netflix[Netflix.Cast == 'Tom Cruise']
Netflix[Netflix.Cast.str.contains('Tom Cruise')]
#We have to drop the null Values.
Netflix_new = Netflix.dropna()
Netflix_new
Netflix_new[Netflix_new.Cast.str.contains('Tom Cruise')]
### Q.9. What are the different Ratings defined by Netflix ?
Netflix.Rating.unique()
#### Q.9.1. How many Movies got the 'TV-14' rating, in Canada ?
Netflix[(Netflix['Category']=='Movie') & (Netflix['Rating']=='TV-14') & (Netflix.Country == 'Canada')]
#### Q.9.2. How many TV Show got the 'R' rating, after year 2018 ?
Netflix[(Netflix.Category == 'TV Show') & (Netflix.Rating == 'R') & (Netflix.Year > 2018)]
### Q.10. What is the maximum duration of a Movie/Show on Netflix ?
Netflix.Duration.unique()
Netflix[['Minutes', 'Unit']] = Netflix['Duration'].str.split(' ', expand = True)
Netflix['Minutes'].max()
### Q.11. Which individual country has the Highest No. of TV Shows ?
Netflix_ = Netflix[Netflix.Category == 'TV Show']
Netflix_
Netflix_.Country.value_counts()
### Q.12. How can we sort the dataset by Year ?
Netflix.sort_values(by = 'Year')
Netflix.sort_values(by = 'Year', ascending = False).head(10)
## Find all the instances where : "Category is 'Movie' and Type is 'Dramas' **OR** Category is 'TV Show' & Type is 'Kids' TV'"
Netflix[(Netflix['Category']=='Movie') & (Netflix['Type']=='Dramas') | (Netflix['Category']=='TV Show') & (Netflix['Type']== "Kids' TV")]

#We Have come to the End.
################################################################################
