#Working on Real Project With Python
#The Housing Dataset
import pandas as pd
House = pd.read_csv(r"C:\Users\user\Projects\Data-Analysis-Projects\Housing Data Analysis\HouseData.csv")
House
#How to Analyze DataFrames
House.head() # for the head of the data
House.shape # for the total number of Rows and Columns
House.index # for the Range of the Data
House.columns # for the names of the Columns
House.dtypes #this show the Kind of data a particular column is
House.nunique() #shows the number of unique values in a table column
# Lets see the Basic information about the Data
House.info()
# Lets look at the Data to see the number of null values in each column
House.isnull().sum()
########################################################################################################
# Lets run some Analysis to view somw certain Updates
# Firstly we would want to see the heatmap of the null values
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(covid.isnull())
plt.show()
# For the Questions Part
#1 Convert the Datatype of 'Date' column to Date-Time format.
House.date = pd.to_datetime(House.date) # To convert a date Column TO a DateTime
#2 Add a new column ''year'' in the dataframe, which contains years only.
House['Year'] = House.date.dt.year
House
#3 Add a new column ''month'' as 2nd column in the dataframe, which contains month only.
#House['Month'] = House.date.dt.month
House.insert(1, 'Month', House.date.dt.month)
House
#4 Remove the columns 'year' and 'month' from the dataframe.
House.drop(['Month', 'Year'], axis = 1, inplace = True)
House.head()
#5 Show all the records where 'No. of Crimes' is 0. And, how many such records are there?
House[House.no_of_crimes == 0]
#6 What is the maximum & minimum 'average_price' per year in england?
House.groupby('Year').average_price.mean()
england = House[House.area == 'england']
england.groupby('Year').average_price.max()
england.groupby('Year').average_price.mean()
#7 What is the Maximum & Minimum No. of Crimes recorded per area?
#data.groupby('area').no_of_crimes.max()
House.groupby('area').no_of_crimes.min().sort_values(ascending = False)
#8 Show the total count of records of each area, where average price is less than 100000.
House[House.average_price < 100000].area.value_counts()
# We have come to the end
##########################################################################################################
