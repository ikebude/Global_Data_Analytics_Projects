#Working on Real Project With Python
#The Cars Dataset
cars = pd.read_csv(r"C:\Users\user\Projects\Data-Analysis-Projects\Cars Data Analysis\CarsDataset.csv")
cars
?cars
#How to Analyze DataFrames
cars.head() # for the head of the data
cars.shape # for the total number of Rows and Columns
cars.index # for the Range of the Data
cars.columns # for the names of the Columns
cars.dtypes #this show the Kind of data a particular column is
cars.nunique() #shows the number of unique values in a table column
# Lets see the Basic information about the Data
cars.info()
# We can see thats theres no null value in each column, the data has been cleaned successfully
########################################################################################################
# Lets run some Analysis to view somw certain things
# 1) Instruction (For Data Cleaning)
# Find all Null Values in the dataset. If there is any null value in any column, then fill it with the mean of that column.
cars.isnull().sum()
# Put the mean of the cylinder column in the null value
cars['Cylinders'].fillna(cars['Cylinders'].mean(), inplace = True)
# 2) Question ( Based on Value Counts )
# Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data
cars.Make.value_counts()
# 3) Instruction ( Filtering )
# Show all the records where Origin is Asia or Europe.
cars[(cars.Origin == 'Asia') | (cars.Origin == 'Europe')]
cars[cars['Origin'].isin(['Asia', 'Europe'])]
# 4) Instruction ( Removing unwanted records )
# Remove all the records (rows) where Weight is above 4000.
cars[~(cars['Weight'] > 4000)]
# 5) Instruction ( Applying function on a column )
# Increase all the values of 'MPG_City' column by 3.
cars['MPG_City'] =  cars['MPG_City'].apply(lambda x:x+3)
cars
------
