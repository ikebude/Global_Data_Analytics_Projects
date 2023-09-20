#Working on Real Project With R
#The Cars Dataset
cars <- read_csv("C:/Users/user/Projects/Data-Analysis-Projects/Cars Data Analysis/CarsDataset.csv")
cars
?cars
#How to Analyze Data Frames
head(cars) # for the head of the data
describe(cars) # for the total number of Rows and Columns
cars |> colnames() # for the names of the Columns
cars |> str() #this show the Kind of data a particular column is
unique(cars$Make)
n_distinct(cars) #shows the number of unique values in a table column
# Lets see the Basic information about the Data
cars |> describe()
cars |> 
  distinct(Make)
# We can see that's there's no null value in each column, the data has been cleaned successfully
########################################################################################################
# Lets run some Analysis to view some certain things
# 1) Instruction (For Data Cleaning)
# Find all Null Values in the data set. If there is any null value in any column, then fill it with the mean of that column.
sum(is.na(cars))
colSums(is.na(cars))
# Put the mean of the cylinder column in the null value
cars$Cylinders[is.na(cars$Cylinders)] <- mean(cars$Cylinders, na.rm = TRUE)
cars |> mutate(Cylinders = replace_na(Cylinders,mean(Cylinders, na.rm = TRUE))) #not working yet
# 2) Question ( Based on Value Counts )
# Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data
cars |> count(Make)
# 3) Instruction ( Filtering )
# Show all the records where Origin is Asia or Europe.
cars |> 
  filter((Origin == "Asia") | (Origin == "Europe"))
# 4) Instruction ( Removing unwanted records )
# Remove all the records (rows) where Weight is above 4000.
cars |> 
  subset((Weight <= 4000))
# 5) Instruction ( Applying function on a column )
# Increase all the values of 'MPG_City' column by 3.
 cars[, "MPG_City"] +3
# add cars <- in front to make it permanent
-----