#!/usr/bin/env python
# coding: utf-8

# ## Project Title: Netflix Data Analytics Project.
# 
# **Task Overview:** The purpose of this project is to analyze the available data that shows all the TV Shows and Movies Available in Netflix till 2021. The Tables Shows a long range of data covering the Directors, The Casts, The length of the TV Show or Movie, THE Release Date as well as the Country'
# 
# This dataset is collected from Flixable which is a third-party Netflix search engine, and available on Kaggle website for free. We are going to analyze the Data frame.
# 
# ## Project Objectives:
# This project will focus on bringing out useful Insights that a Manager can Read into Knowing How Much of A Particular variable is in the Dataset.

# In[2]:


import pandas as pd


# In[3]:


Netflix = pd.read_csv(r"C:\Users\user\Projects\Data-Analysis-Projects\Netflix Data Analytics\Netflix-Dataset.csv")


# In[4]:


Netflix


# ### How to Analyze DataFrames

# In[5]:


Netflix.head() # for the head of the data


# In[6]:


Netflix.shape # for the total number of Rows and Columns


# In[7]:


Netflix.index # for the Range of the Data


# In[8]:


Netflix.columns


# In[9]:


Netflix.dtypes #this show the Kind of data a particular column is


# In[10]:


Netflix.nunique()


# In[11]:


Netflix.info()


# ### Lets run some Analysis to view somw certain Updates
# #### For the Questions Part

# ### Task.1. Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.

# In[12]:


Netflix[Netflix.duplicated()]


# In[13]:


Netflix.drop_duplicates(inplace = True)


# ### Task.2. Is there any Null Value present in any column ? Show with Heat-map.

# In[14]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[15]:


sns.heatmap(Netflix.isnull())


# ### Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show?

# In[16]:


Netflix[Netflix.Title == 'House of Cards']


# In[17]:


Netflix[Netflix['Title'].str.contains('House of Cards')]          #  To show all records of a particular string in any column


# ### Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# In[18]:


Netflix['Date'] = pd.to_datetime(Netflix['Release_Date'])


# In[21]:


Netflix.dtypes


# In[20]:


Netflix['Year'] = Netflix.Date.dt.year


# ### Value Counts

# In[22]:


Netflix.Year.value_counts().plot(kind = 'bar')


# ### Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# In[26]:


Netflix['Category'].value_counts()


# ### Q.4. Show all the Movies that were released in year 2020.

# In[27]:


Netflix[(Netflix.Category == 'Movie') & (Netflix.Year == 2020)]


# ### Q.5. Show only the Titles of all TV Shows that were released in India only.

# In[28]:


Netflix[(Netflix.Category == 'TV Show') & (Netflix.Country == 'India')] ['Title']


# ### Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# In[29]:


Netflix.Director.value_counts().head(10)


# #### Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".

# In[30]:


# Using String Contains
Netflix[(Netflix.Category == 'Movie') & (Netflix.Type.str.contains('Comedies')) | (Netflix.Country == 'United Kingdom')]


# In[31]:


#Using Filtering
Netflix[(Netflix.Category == 'Movie') & (Netflix.Type == 'Comedies') | (Netflix.Country == 'United Kingdom')]


# ### Q.8. In how many movies/shows, Tom Cruise was cast?

# In[32]:


Netflix[Netflix.Cast == 'Tom Cruise']


# In[33]:


Netflix[Netflix.Cast.str.contains('Tom Cruise')]


# ### We have to drop the null Values.

# In[34]:


Netflix_new = Netflix.dropna()


# In[35]:


Netflix_new[Netflix_new.Cast.str.contains('Tom Cruise')]


# ### Q.9. What are the different Ratings defined by Netflix ?

# In[36]:


Netflix.Rating.unique()


# #### Q.9.1. How many Movies got the 'TV-14' rating, in Canada ?

# In[37]:


Netflix[(Netflix['Category']=='Movie') & (Netflix['Rating']=='TV-14') & (Netflix.Country == 'Canada')]


# #### Q.9.2. How many TV Show got the 'R' rating, after year 2018 ?

# In[38]:


Netflix[(Netflix.Category == 'TV Show') & (Netflix.Rating == 'R') & (Netflix.Year > 2018)]


# ### Q.10. What is the maximum duration of a Movie/Show on Netflix?

# In[39]:


Netflix.Duration.unique()


# In[40]:


Netflix[['Minutes', 'Unit']] = Netflix['Duration'].str.split(' ', expand = True)


# In[41]:


Netflix['Minutes'].max()


# ### Q.11. Which individual country has the Highest No. of TV Shows ?

# In[42]:


Netflix_ = Netflix[Netflix.Category == 'TV Show']


# In[43]:


Netflix_


# In[44]:


Netflix_.Country.value_counts()


# ### Q.12. How can we sort the dataset by Year ?

# In[45]:


Netflix.sort_values(by = 'Year', ascending = False).head(10) # The head is not compulsory


# ### 13. Find all the instances where : "Category is 'Movie' and Type is 'Dramas' **OR** Category is 'TV Show' & Type is 'Kids' TV'"

# In[47]:


Netflix[(Netflix['Category']=='Movie') & (Netflix['Type']=='Dramas')]


# In[49]:


Netflix[(Netflix['Category']=='TV Show') & (Netflix['Type']== "Kids' TV")]


# In[51]:


Netflix[(Netflix['Category']=='Movie') & (Netflix['Type']=='Dramas') | (Netflix['Category']=='TV Show') & 
        (Netflix['Type']== "Kids' TV")]


# #### We Have come to the End.

# # By Precious Ikebude
