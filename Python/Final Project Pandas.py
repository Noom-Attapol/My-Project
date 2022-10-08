# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 17 September 2022
# 
# **Author**: Attapol Aiempichitkijkarn (Noom)
# 
# **Course**: `Pandas Foundation`


# import data
import pandas as pd
import numpy as np
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(10), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframe
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df.info()

# TODO - count nan in postal code column
# df.isna().sum()
df['Postal Code'].isna().sum()

# TODO - filter rows with missing values
clean_df = df.dropna()
clean_df.shape
df.head()
#df = clean_df

# TODO - Explore this dataset on your owns, ask your own questions
# How Many Segment in this Dataset and Amount of each segment
df['Segment'].value_counts()

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
# Answer 01 : This Data set have 21 columns and 9994 rows
df.shape

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
# Answer 02 : There are 11 missing values in column 'Postal Code' 
df.isna().sum()

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
# Answer 03 :
#df[['Country/Region','City','State']].head(20)
df_California = df[df['State'] == 'California']
df_California.to_csv('df_california.csv')

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
# Answer 04 : 
df_CaliTexa = df.query('State == "California" or State == "Texas"')
df_CaliTexa_2017 = df_CaliTexa[df_CaliTexa['Order Date'].dt.to_period('Y') == '2017']
df_CaliTexa_2017.to_csv('df_CaliTexa_2017.csv')

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
# Answer 05 :
df_2017 = df[df['Order Date'].dt.to_period('Y') == '2017']
df_2017_totalsales = df_2017['Sales'].sum()
df_2017_avgsales = df_2017['Sales'].mean()
df_2017_stddev = df_2017['Sales'].std()
print(f"Total sales in 2017 = {df_2017_totalsales}")
print(f"Average sales in 2017 = {df_2017_avgsales}")
print(f"Standard deviation in 2017 = {df_2017_stddev}")
df_2017['Sales'].describe()

# TODO 06 - which Segment has the highest profit in 2018
# Answer 06 : Consumer Segment has the highest profit in 2018
df_2018 = df[df['Order Date'].dt.to_period('Y') == '2018']
df_2018.groupby('Segment')['Profit'].sum()

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
# Answer 07 :   1.California    2.New York   3.Texas    4.Pennsylvania   5.Michigan                
df_07 = df[(df['Order Date'] > '2019-04-15') & (df['Order Date'] < '2019-12-31')]
df_07_sum = df_07.groupby('State')['Sales'].sum()
df_07_sum.sort_values(ascending=False)

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
# Answer 08 = 55.24 %
df_2019 = df[df['Order Date'].dt.to_period('Y') == '2019']
df_2019_totRegion = df_2019['Sales'].sum()
df_2019_WC = df_2019.query('Region == "West" | Region == "Central"')['Sales'].sum()
result_08 = df_2019_WC/df_2019_totRegion * 100
print(f"The Proportion of total Sales(%) in West + Central in 2019 = {result_08} %")

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
# Answer 09 =
df_09 = df[(df['Order Date'] > '2018-12-31') & (df['Order Date'] < '2021-01-01')]
result09_Q = df_09.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False)
result09_Q.head(10)
result09_S = df_09.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)
result09_S.head(10)

# TODO 10 - plot at least 2 plots, any plot you think interesting :)
# Answer 10.1 = Bar Chart of Top 10 Products in Term of Quantity 
result09_Q.head(10).plot(kind='bar')

#Answer 10.2 = 
df_sum_region = df.groupby('Region')['Sales'].sum()
df_sum_region.plot(kind='pie')

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
df_append = df
df_append['Status Profit'] = np.where(df_append['Profit'] > 0 ,'Profit', 'Lost')
lost_profit = df_append[df_append['Status Profit'] == 'Lost']
#lost_profit.head()
lost_profit[['Order ID', "Order Date", "Profit" , "Status Profit"]]

