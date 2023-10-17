#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First we import BeautifulSoup to prettify data

from bs4 import BeautifulSoup 
import requests


# In[2]:


#Now we set the url variable equal to the url, bring the page at, and bring it at this time ('html')

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue#:~:text=List%20of%20the%20largest%20companies%20%20%20,%20%2032.0%25%20%2023%20more%20rows%20'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)


# In[3]:


#Next we're going to find the table that we want via inspection

soup.find('table' , class_= 'wikitable sortable')


# In[6]:


#Now that we know which table it is we now set equal to our origin table

table = soup.find_all('table')[1]

#WIth one indicating this is the 2nd instance of a tabel


# In[7]:


print(table)


# In[9]:


#Alright now that we've set this equal to the original table we can now modify it

world_titles = table.find_all('th') #Grouping all th tags

world_table_titles = [title.text.strip() for title in world_titles] #Removing th tags

print(world_table_titles)


# In[ ]:





# # Pandas Portion 

# In[10]:


#Now that we've have the column titles we can now create our dataframe via pandas

import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

df


# In[11]:


#Now that we have the column titles in the data frame we can now set the rest of the information in:

column_data = table.find_all('tr') 

for row in column_data[1:]:
    row_data = row.find_all('td') #Grouping all td tags
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] =  individual_row_data
    
df


# In[ ]:





# # Exporting to excel csv file

# In[13]:


#Now that we've finished dataframe we can export as excel csv file:

df.to_csv(r'C:\Users\hands\OneDrive\Documents\Python Webscraping/Companieseeses.csv', index = False)

#Where r indicates raw text.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




