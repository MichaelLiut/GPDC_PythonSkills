"""
	Introduction to Python Program File
"""

## Import Dependencies/Packages ##

import pandas, datetime, itertools
from pandas import DataFrame
from datetime import date 
import random , numpy, math, array, h5py
import time
import matplotlib.pyplot as plt 
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

## Import CSV as DataFrame ##

data = pandas.read_csv(r'KO.csv')

## DataFrame Manipulation ##

data = data.drop(columns="Volume") # Drop Fields #

data = data.rename(columns = {"Date": "Trading_Date"}) # Rename Fields # 
							           # New Name # 
print(data) # see output # 

columns = data.columns # Identify columns names #

data = data.sort_values(by = 'Trading_Date',ascending = True) # Sort dataset by Trading Date # 

data_subset = data[['Trading_Date','Close']] # subset columns #

data_subset = data_subset[:100] # subset rows # 

## Create Variables ##

open_close_ratio = data.Open / data.Close
data["Open_Close_Price_Ratio"] = open_close_ratio

high_low_price_dif = data.High - data.Low
data["High_Low_Price_Diff"] = high_low_price_dif

year = data.Trading_Date.str.slice(0,4) # Trading Year #
month = data.Trading_Date.str.slice(5,7) # Trading Month #
day = data.Trading_Date.str.slice(8,10) # Trading Day # 

## Adding fields to original dataset ## 
data['year'] = year 
data['month'] = month
data['day'] = day

## Define Function for Evaluating the ratio between Open and Close Prices for a Stock ## 
def open_close_evaluation(variable):
	for i in open_close_ratio:
		if i > 1:
			variable.append('Open_Price_Higher')
		else:
			variable.append('Open_Price_Lower')

open_close_price_label = [] # Initialize new field 
open_close_evaluation(open_close_price_label) # Execute function 
print(open_close_price_label) # print output 
data['Open_Close_Price_Ratio_Label'] = open_close_price_label # add to original dataset 

## Summary Statistics ##

pandas.DataFrame.head(data) # First few rows of data for observation 
descriptive_metrics = pandas.DataFrame.describe(data) # Key Metrics 
correlation = pandas.DataFrame.corr(data,method = 'pearson') # Correlation 
data.Open_Close_Price_Ratio_Label.value_counts() # Counts the number of elements within a particular field 
len(data) # number of observations #
len(data.columns) # number of columns 
min(data.Open) # minimum Open Price # 
min(data.Close) # minimum Close Price # 
max(data.Open) # Max Open Price # 
max(data.Close) # Max Close Price # 

## Plot Close Price Over Time ##

x = data.Trading_Date
x = pandas.to_datetime(x) # Convert to datetime format for graphing #
y = list(data.Close)
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%Y')

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x,
        y,
        color='green')
ax.set(xlabel="Date", ylabel="Closing Prices",
       title="Closing Price Trend Over Time")

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

# format coordinates #
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

ax.grid(True)
fig.autofmt_xdate()
plt.show()

## Plot bar graph of one data field ##

label = ['Open_Price_Lower','Open_Price_Higher'] # Create x - axis # 

## Subsetting datas field based on criteria ## 
# Value Count # 
label1 = len(data[data.Open_Close_Price_Ratio_Label == 'Open_Price_Lower'])  
# Value Count # 
label2 = len(data[data.Open_Close_Price_Ratio_Label == 'Open_Price_Higher']) 

values = [label1,label2] # Create y-axis # 

plt.bar(label,values,width = 0.8, align = 'center') # Create plot # 
plt.title('Analysis of Open to Close Price Ratios')
plt.xlabel('Categories')
plt.ylabel('Frequency')

# Delete unnecessary fields #

del day,month,year,high_low_price_dif,open_close_price_label,open_close_ratio

## Export to CSV ##

today_date = date.today()
url = 'datafile_%s.csv' %(today_date)
data.to_csv(url)
