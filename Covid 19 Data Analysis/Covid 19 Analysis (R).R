#Working on Real Project With Python
#The Covid 19 Dataset
covid <- read_csv("C:/Users/user/Projects/Data-Analysis-Projects/Covid 19 Data Analysis/CovidData.csv")
covid
#How to Analyze DataFrames
head(covid) # for the head of the data
describe(covid) # for the total number of Rows and Columns
range(covid) # for the Range of the Data
covid |> colnames() # for the names of the Columns
covid |> str() #this show the Kind of data a particular column is
covid.nunique() #shows the number of unique values in a table column
# Lets see the Basic information about the Data
unique(covid$Recovered)
# Lets look at the Data to see the number of null values in each column
is.na(covid) |> sum()
########################################################################################################
# Lets run some Analysis to view somw certain Updates
# Firstly we would want to see the heatmap of the null values
sns.heatmap(covid.isnull())
plt.show()
# Q.1 ) Show the number of Confirmed , Deaths and Recovered cases in each Region.
covid |> group_by(Region) |> reframe(sum(Confirmed), sum(Deaths), sum(Recovered)) |> arrange(desc(`sum(Deaths)`))
covid |> group_by(Region) |> reframe(Confirmed, Deaths, Recovered)
covid |> group_by(Region)
# Q2) Remove all the records where Confirmed Cases is Less Than 10.
covid19 <- covid |> filter(Confirmed > 10)
### Q.3) In which Region, maximum number of Confirmed cases were recorded ?
covid |> group_by(Region) |> summarise(Confirmed = sum(Confirmed)) |> arrange(desc(Confirmed)) |> print(n = 5)
# Q.4) In which Region, minimum number of Deaths cases were recorded ?
covid |> group_by(Region) |> summarise(Deaths = sum(Deaths)) |> arrange(Deaths) |> print(n = 5)
# Q.5) How many Confirmed , Deaths & Recovered cases were reported from India till 29 April 2020?
covid |> filter(Region == 'India')
covid |> filter(Region == 'US') 
# Q. 6-A ) Sort the entire data wrt No. of Confirmed cases in ascending order
covid |> arrange(Confirmed)
# Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.
covid |> arrange(desc(Recovered))
covid19 |> arrange(desc(Recovered))
# We have come to the end
##########################################################################################################
covid |> group_by(Region) |> summarise(Confirmed = sum(Confirmed)) |> arrange(desc(Confirmed)) |> filter(Region == 'US')
