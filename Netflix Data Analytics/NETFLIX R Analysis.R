#Working on Real Project With R
#The NetFlix Dataset
Netflix <- read_csv("C:/Users/user/Projects/Data-Analysis-Projects/Netflix Data Analytics/Netflix-Dataset.csv")
Netflix
#How to Analyze DataFrames
head(Netflix) # for the head of the data
nrow(Netflix) # for the total number of Rows and Columns
ncol(Netflix) # for the Range of the Data
Netflix |> colnames() # for the names of the Columns
str(Netflix) #this show the Kind of data a particular column is
Netflix |> n_distinct() #shows the number of unique values in a table column
# Lets see the Basic information about the Data
Netflix |> describe()
# Lets look at the Data to see the number of null values in each column
Netflix |> is.na() |> colSums()
########################################################################################################
# Lets run some Analysis to view somw certain Updates
# For the Questions Part
### Task.1. Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.
duplicated(Netflix)
Netflix[duplicated(Netflix),]
Netflix <- Netflix[!duplicated(Netflix),]
Netflix
### Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show?
Netflix |>  filter(Title == 'House of Cards')
#OR
Netflix |> filter(grepl('House of Cards', Title))       #  To show all records of a particular item in any column
### Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.
Netflix$Release_Date <- dmy(Netflix$Release_Date)
Netflix
Netflix <- Netflix |> mutate(Year = year(Netflix$Release_Date))
# Value Counts
Netflix$Year |> n_distinct()
Netflix |> count(Year)
plot(Netflix$Year)
### Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph.
n_distinct(Netflix$Category)
Netflix |> count(Category)
### Q.4. Show all the Movies that were released in year 2020.
Netflix |> filter((Category == 'Movie') & (Year = 2020))
### Q.5. Show only the Titles of all TV Shows that were released in India only.
Netflix |> filter((Category == 'TV Show') & (Country == 'India')) |> select(Title)
### Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?
Netflix |> count(Director) |> arrange(desc(n))
#### Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
Netflix |> filter((Category == 'Movie') & (Type == 'Comedies') | (Country == 'United Kingdom'))
Netflix |> filter((Category == 'Movie') & (grepl('Comedies', Type)) | (Country == 'United Kingdom'))
### Q.8. In how many movies/shows, Tom Cruise was cast?
Netflix |> filter(Cast == 'Tom Cruise')
Netflix |> filter(grepl('Tom Cruise', Cast))
#We have to drop the null Values.
Netflix_new <- na.omit(Netflix)
Netflix_now <- Netflix[complete.cases(Netflix),]
### Q.9. What are the different Ratings defined by Netflix ?
unique(Netflix$Rating)
#### Q.9.1. How many Movies got the 'TV-14' rating, in Canada ?
Netflix |> filter((Category =='Movie') & (Rating =='TV-14') & (Country == 'Canada'))
#### Q.9.2. How many TV Show got the 'R' rating, after year 2018 ?
Netflix |> filter((Category == 'TV Show') & (Rating == 'R') & (Year > 2018))
### Q.10. What is the maximum duration of a Movie/Show on Netflix ?
library(stringr)
Netflix[c('Minutes','Units')] <- str_split_fixed(Netflix$Duration, ' ', 2)
Netflix
max(Netflix$Minutes)
####################################################
Netflix_now |> separate(Duration, c('Minutes', 'Units'))
### Q.11. Which individual country has the Highest No. of TV Shows ?
Netflix_ <- Netflix |> filter(Category == 'TV Show')
Netflix_
Netflix_ |> count(Country) |> arrange(desc(n))
### Q.12. How can we sort the dataset by Year ?
Netflix |> arrange(Year)
Netflix |> arrange(desc(Year))
## Find all the instances where : "Category is 'Movie' and Type is 'Dramas' **OR** Category is 'TV Show' & Type is 'Kids' TV'"
Netflix |> filter((Category =='Movie') & (Type =='Dramas') | (Category =='TV Show') & (Type == "Kids' TV"))
#We Have come to the End.
################################################################################