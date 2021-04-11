#!/usr/bin/env python
# coding: utf-8

# In[149]:


# Author: Subah Sachdeva
# IS362: Project 1
# Professor Pak

# load pandas libraries as 'pd'
import pandas as pd

# read csv arrival_delays.csv and exclude the first two columns to only read from Los Angeles 
# to Seattle, also filter NaN fields that are empty by setting a filter
df_csv = pd.read_csv('arrival_delays.csv',na_filter= False, skipinitialspace=True, index_col=[0,1])

# write to csv by setting mode to 'w'
df_csv.to_csv('arrival_delays.csv', index=True, mode= 'w')

# read csv again to output values to compute for total sum of 
# delayed flights for each airline
df_csv = pd.read_csv('arrival_delays.csv',na_filter= False, skipinitialspace=True, index_col=[0,1])

# Gather each row starting from where column reads 'Los Angeles' but equals '62' and '117' 
# so we grab the correct row of values to sum up
alaska_delays_row = (data[data['Los Angeles'] == '62']).sum()
amwest_delays_row = (data[data['Los Angeles'] == '117']).sum()

# place the totals into each var 
alaska_total = alaska_delays_row.sum()
amwest_total = amwest_delays_row.sum()
total = alaska_total + amwest_total

# calculate the percentage for each airline
alaska_percentage = alaska_total / total * 100
amwest_percentage = amwest_total / total * 100

# append this new information to the very last column 'Total Delays' that also lines up with 
# preset rows named 'complete % of delayed flights for..'

df_csv['Total Delays'] = ['', alaska_total, "{0:.0f}%".format(alaska_percentage), '', amwest_total, "{0:.0f}%".format(amwest_percentage), total]

# Reading the final output:
# We can see that AM WEST has over 20% more delayed flights than ALASKA

df_csv.head(9)


# In[ ]:





# In[ ]:




