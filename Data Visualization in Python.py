import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Netflix = pd.read_csv(r"C:\Users\user\Projects\Data-Analysis-Projects\Netflix Data Analytics\Netflix-Dataset.csv")
Netflix['Release_Date'] = pd.to_datetime(Netflix['Release_Date'])
Netflix['Year'] = Netflix.Release_Date.dt.year
Netflix[['Minutes','Units']] = Netflix.Duration.str.split(' ', expand = True)
Netflix.plot.bar(x = ['Category'], y = value_counts(Netflix.Category))
plt.plot.bar(x = Netflix.category,)
plt.bar(Netflix.Category,Netflix.Minutes)
plt.show()
Netflixx = Netflix[Netflix.Category == 'TV Show']
plt.bar(Netflixx['Units'], Netflixx['Minutes'])
plt.show()
quit
Country = ['Usa' , 'Canada' , 'Australia' , 'India']
Cases = [45000 , 25000 , 33000 , 53000]
Colours = ['green' , 'blue' , 'purple' , 'teal']
plt.bar(Country,Cases,color = Colours)
plt.show()

plt.close()
Iris = pd.read_csv('Iris.csv')
plt.hist(Netflixx.Minutes, bins = 30)
plt.show()
plt.boxplot(Netflixx.Units, labels=Netflixx)
plt.boxplot(Cases)
plt.show()
Netflixc =Netflix[Netflix.Category == 'Movie']
plt.boxplot(Netflixc.Minutes)
Netflix.dtypes
Netflix.Minutes = pd.to_numeric(Netflix.Minutes)
plt.violinplot(Netflixx.Minutes)
plt.show()
plt.pie(Netflixx.Minutes)
plt.show()
plt.close()
range(Netflix.Minutes)
plt.pie(Netflix['Minutes'], labels = Netflix.Category)
sum(Netflix.Minutes)
plt.stackplot(Netflixx.Year,Netflixx.Minutes)
plt.show()
quit
Economics = r.economics
plt.plot(Economics.date,Economics.unemploy)
Economics.dtypes
Economics.date = pd.to_datetime(Economic.date)
plt.show()







