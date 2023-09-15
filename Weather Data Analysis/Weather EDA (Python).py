#Working on Real Project With Python
#The Weather Dataset
Weather = pd.read_csv(r"C:\Users\user\Projects\Data Analytics Projects\Weather Data Analysis\WeatherDataset.csv")
Weather
?Weather
#How to Analyze DataFrames
#1 The First N rows in the Data (By default N=5)
Weather.head()
#2 The Total Number of Rows and Columns of the dataframe
Weather.shape
#3 The Index of a Dataframe
Weather.index
#4 The Names of each Column
Weather.columns
#5 The Datatypes of each Colum
Weather.dtypes
#6 In a Column, Show all The Unique Values. It can be only applied to a single column and not the whole dataframe
Weather["Weather"].unique()
#7 Show the total number of unique values in each column. It can be applied on a single column and also the entire dataframe
Weather["Weather"].nunique()
Weather.nunique()
#8 SHow the total number of non-null Values in each column. It can be applied in both the Dataframe and a single column
Weather["Weather"].count()
Weather.count()
#9 Showing all unique Values with their count. It can be applied on a single column only
Weather["Weather"].value_counts()
#10 Provide Basic Information About The Data Frame
Weather.info()
#############################################################################################
#Lets Dive into Answering Some Useful Analysis Questions
#Q1 Find all the Unique "windspeed" Values in the Data
Weather["Wind Speed_km/h"].unique()
Weather["Wind Speed_km/h"].nunique()
Weather.nunique()
#Q2 Find the number of times when the "Weather is Exactly Clear"
Weather["Weather"].value_counts()
Weather[Weather.Weather == 'Clear']
Weather.groupby('Weather').get_group('Clear')
#Q3 Find the number of times when the wind speed was exactly "4 Km/h"
Weather.head(2)
Weather[Weather["Wind Speed_km/h"] == 4]
#Q4 Find out the Null Values in The Data
Weather.isnull().sum()
Weather.notna().sum()
#Q5 Rename the column "Weather" of the Dataframe to 'Weather Conditions'
Weather.rename(columns = {'Weather_Condition' : 'Weather'}, inplace = True) # inplace = True for permanently
#Q6 What is the Mean Visibility ?
WeatherDataset.columns
Weather.Visibility_km.mean()
#Q7 What is the Standard Deviation Of 'Pressure' in this Data?
Weather.Press_kPa.std()
#Q8 What is the variance of 'Relative Humidity' in this Data
Weather['Rel Hum_%'].var()
#Q9 Find all instances when Snow was Recorded
Weather.Weather.value_counts()
Weather[Weather.Weather == 'Snow']
Weather[Weather.Weather.str.contains('Snow')]
Weather.Weather.str.contains('Snow').value_counts()
#Q10 Find all instances when 'wind Speed is above 24' and 'Visibility is 25'
Weather[(Weather['Wind Speed_km/h'] > 24) & (Weather['Visibility_km'] == 25)]
#Q11 What is the mean value of each column against each weather conditions
Weather.groupby('Weather_Condition')
Weather
WeatherWeather.groupby('Weather_Condition').mean()
Weather.drop('Date/Time', axis=1).groupby('Weather_Condition').mean()
#Q12 What is the Minimum & maximum value of each column against each weather condition
Weather.groupby('Weather_Condition').min()
Weather.groupby('Weather_Condition').max()
#Q13 Show all the Record where Weather Codition is Fog.
Weather[Weather['Weather_Condition'] == 'Fog']
#Q14 Find all Instances When 'Weather is Clear' or visibility is above 40
Weather[(Weather['Weather_Condition'] == 'Clear') | (Weather['Visibility_km'] > 40)]
#Q15 Find all instances when
#A Weather is Clear and Relatively Humidity is greater than 50
#or
#B Visibility is Above 40
Weather[(Weather['Weather_Condition'] == 'Clear') & (Weather['Rel Hum_%'] > 50) | (Weather['Visibility_km'] > 40) ]
#The End
-------------------------------------------------------------------------------------------------------------------
