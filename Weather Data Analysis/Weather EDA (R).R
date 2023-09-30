#Working on Real Project With R
#The Weather Dataset
WeatherDataset <- read_csv("C:/Users/user/Projects/Data Analytics Projects/Weather Data Analysis/WeatherDataset.csv")
View(WeatherDataset)
#How to Analyze DataFrames
#1 The First N rows in the Data (By default N=5)
WeatherDataset |> 
  head()
#2 The Total Number of Rows and Columns of the dataframe
WeatherDataset |> 
  nrow()
WeatherDataset |> 
  ncol()
#3 The Index of a Dataframe
# Dataframes in R do not have an 'index' column like dataframes in pandas might
#4 The Names of each Column
WeatherDataset |> 
  colnames()
WeatherDataset |> 
  rownames()
#5 The Datatypes of each Colum
WeatherDataset |> 
  str()
#6 In a Column, Show all The Unique Values. It can be only applied to a single column and not the whole dataframe
WeatherDataset |> 
  filter(!duplicated(Weather))
unique(WeatherDataset$Weather)
WeatherDataset |> 
  distinct(Weather) |> 
  print(n = 50)
#7 Show the total number of unique values in each column. It can be applied on a single column and also the entire dataframe
WeatherDataset$Weather |> 
  n_distinct()
n_distinct(WeatherDataset$Weather)
#8 SHow the total number of non-null Values in each column. It can be applied in both the Dataframe and a single column
sum(is.na(WeatherDataset$Weather))
sum(is.na(WeatherDataset))
#9 Showing all unique Values with their count. It can be applied on a single column only
WeatherDataset |> 
  count()
#10 Provide Basic Information About The Data Frame
WeatherDataset |> 
  describe()
#############################################################################################
#Lets Dive into Answering Some Useful Analysis Questions
#Q1 Find all the Unique "windspeed" Values in the Data
unique(WeatherDataset$`Wind Speed_km/h`)
WeatherDataset |> 
  count(`Wind Speed_km/h`)
#Q2 Find the number of times when the "Weather is Exactly Clear"
WeatherDataset |> 
  count(Weather) |> 
  filter(Weather == 'Clear')
#Q3 Find the number of times when the wind speed was exactly "4 Km/h"
WeatherDataset |> 
  count(`Wind Speed_km/h`)
WeatherDataset |> 
  count(`Wind Speed_km/h`) |> 
  filter(`Wind Speed_km/h` == 4)
#Q4 Find out the Null Values in The Data
colSums(is.na(WeatherDataset))
WeatherDataset |> 
  is.null()
#Q5 Rename the column "Weather" of the Dataframe to 'Weather Conditions'
WeatherDataset |> 
  rename('Weather_Dataset' = 'Weather')
                                       # inplace = True for permanently
#Q6 What is the Mean Visibility ?
WeatherDataset |> 
  describe()
mean(WeatherDataset$Visibility_km)
WeatherDataset |> 
  pull(Visibility_km) |> 
  mean()
#Q7 What is the Standard Deviation Of 'Pressure' in this Data?
WeatherDataset |> 
  pull(Press_kPa) |> 
  sd()
sd(WeatherDataset$Press_kPa)
#Q8 What is the variance of 'Relative Humidity' in this Data
var(WeatherDataset$`Rel Hum_%`)
WeatherDataset |> 
  pull('Rel Hum_%') |> 
  var()
#Q9 Find all instances when Snow was Recorded
WeatherDataset |> 
  filter(Weather == 'Snow')
WeatherDataset |> 
  select(Weather, contains('S'))
WeatherDataset |> 
  filter(grepl('Snow', Weather)) |> 
  count()
#Q10 Find all instances when 'wind Speed is above 24' and 'Visibility is 25'
WeatherDataset |> 
  filter((Visibility_km == 25) & (`Wind Speed_km/h` > 24))
#Q11 What is the mean value of each column against each weather conditions
WeatherDataset |> 
  sapply(mean, simplify = FALSE)
WeatherDataset |> 
  group_by(Weather) |> 
  summarise(mean_Temp = mean(Temp_C))
WeatherDataset |> 
  group_by(Weather) |> 
  summarise(across(Temp_C:Press_kPa, mean))
WeatherDataset |> 
  group_by(Weather) |> 
  summarise_at(vars('Temp_C', 'Press_kPa'), mean)
#Q12 What is the Minimum & maximum value of each column against each weather condition
WeatherDataset |> 
  group_by(Weather) |> 
  summarise(across(Temp_C:Press_kPa, min))
WeatherDataset |> 
  group_by(Weather) |> 
  summarise(across(Temp_C:Press_kPa, max))
#Q13 Show all the Record where Weather Codition is Fog.
WeatherDataset |> 
  filter(Weather == 'Fog')
WeatherDataset |> 
  filter(grepl('Fog', Weather))
#Q14 Find all Instances When 'Weather is Clear' or visibility is above 40
WeatherDataset |> 
  filter((Visibility_km > 40) & (Weather == 'Clear'))
#Q15 Find all instances when
#A Weather is Clear and Relatively Humidity is greater than 50
#or
#B Visibility is Above 40
WeatherDataset |> 
  filter((Weather == 'Clear') & (`Rel Hum_%` > 50) | (Visibility_km > 40))
#The End
-------------------------------------------------------------------------------------------------------------
