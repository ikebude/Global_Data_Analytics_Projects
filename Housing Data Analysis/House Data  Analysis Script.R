#Working on Real Project With R
#The Housing Dataset
House <- read_csv("C:/Users/user/Projects/Data-Analysis-Projects/Housing Data Analysis/HouseData.csv")
House
view(House)
#How to Analyze DataFrames
head(House) # for the head of the data
nrow(House) # for the total number of Rows and Columns
ncol(House) # for the Range of the Data
colnames(House) # for the names of the Columns
str(House) #this show the Kind of data a particular column is
n_distinct(House) #shows the number of unique values in a table column
# Lets see the Basic information about the Data
describe(House)
# Lets look at the Data to see the number of null values in each column
is.na(House) |> colSums()
########################################################################################################
# Lets run some Analysis to view somw certain Updates
# For the Questions Part
#1 Convert the Datatype of 'Date' column to Date-Time format.
House$date <- mdy(House$date)# To convert a date Column TO a DateTime
#2 Add a new column ''year'' in the dataframe, which contains years only.
House <- House |> mutate(Year = year(House$date))
#3 Add a new column ''month'' as 2nd column in the dataframe, which contains month only.
House |>  mutate(Month = month(House$date))
House |> mutate(Month = month.name[month(House$date)])
#4 Remove the columns 'year' and 'month' from the dataframe.
House |> select(-c(no_of_crimes))
House[,-3] #Using Base R
#5 Show all the records where 'No. of Crimes' is 0. And, how many such records are there?
House |> filter(no_of_crimes == 0)
#6 What is the maximum & minimum 'average_price' per year in england?
House |> filter(area == 'england') |> group_by(Year) |> summarise(Min = min(average_price), Max = max(average_price), Mean = mean(average_price))
#7 What is the Maximum & Minimum No. of Crimes recorded per area?
#data.groupby('area').no_of_crimes.max()
House |> group_by(area) |> reframe(Min = min(no_of_crimes, na.rm = TRUE), Max = max(no_of_crimes, na.rm = TRUE), Mean = mean(no_of_crimes, na.rm = TRUE)) |> arrange(Min)
#8 Show the total count of records of each area, where average price is less than 100000.
House |> filter(average_price < 100000) |> count(area)
# We have come to the end
##########################################################################################################
