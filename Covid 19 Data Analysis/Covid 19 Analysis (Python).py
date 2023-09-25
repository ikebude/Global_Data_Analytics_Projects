#Working on Real Project With Python
#The Covid 19 Dataset
covid = pd.read_csv(r"C:\Users\user\Projects\Data-Analysis-Projects\Covid 19 Data Analysis\CovidData.csv")
covid
#How to Analyze DataFrames
covid.head() # for the head of the data
covid.shape # for the total number of Rows and Columns
covid.index # for the Range of the Data
covid.columns # for the names of the Columns
covid.dtypes #this show the Kind of data a particular column is
covid.nunique() #shows the number of unique values in a table column
# Lets see the Basic information about the Data
covid.info()
# Lets look at the Data to see the number of null values in each column
covid.isnull().sum()
########################################################################################################
# Lets run some Analysis to view somw certain Updates
# Firstly we would want to see the heatmap of the null values
sns.heatmap(covid.isnull())
plt.show()
# Q.1 ) Show the number of Confirmed , Deaths and Recovered cases in each Region.
covid.groupby('Region').sum()
covid.groupby('Region')['Confirmed'].sum().sort_values(ascending = False).head(10)
# Q2) Remove all the records where Confirmed Cases is Less Than 10.
covid.Confirmed < 10
covid[covid.Confirmed < 10]
covid[~(covid.Confirmed < 10)]
### Q.3) In which Region, maximum number of Confirmed cases were recorded ?
covid.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(5)
# Q.4) In which Region, minimum number of Deaths cases were recorded ?
covid.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)
# Q.5) How many Confirmed , Deaths & Recovered cases were reported from India till 29 April 2020?
covid[covid.Region == 'India']
covid[covid.Region == 'US'].sum()
# Q. 6-A ) Sort the entire data wrt No. of Confirmed cases in ascending order
covid.sort_values( by = ['Confirmed'] , ascending = True).head(50)
# Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.
covid.sort_values( by = ['Recovered'] , ascending = False).head(50)
# We have come to the end
##########################################################################################################
