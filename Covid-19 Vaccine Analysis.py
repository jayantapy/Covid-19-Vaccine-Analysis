#!/usr/bin/env python
# coding: utf-8

# ## Importing the libraries needed

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv('country_vaccinations.csv')


# In[3]:


data.head()


# ### Now let’s explore this data before we start analyzing the vaccines taken by countries:

# In[4]:


data.describe()


# In[5]:


pd.to_datetime(data.date)
data.country.value_counts()


# The United Kingdom is made up of England, Scotland, Wales, and Northern Ireland. But in the above data, these countries are mentioned separately with the same values as in the United Kingdom. So this may be an error while recording this data. So let’s see how we can fix this error:

# In[6]:


data= data[data.country.apply(lambda x : x not in ['England','Scotland','Wales','Northern Ireland'])]
data.country.value_counts()


# #### Available Vaccines

# In[7]:


data.vaccines.value_counts()


# #### Selecting only the 'country' and 'vaccines' columns from the entire dataset and creating a new dataframe 

# In[8]:


df = data[['country','vaccines']]
df.head()


# Now let’s see how many countries are taking each of the vaccines mentioned in this data:

# In[9]:


d = {}
for i in df.vaccines.unique():
    d[i] = [df['country'][j] for j in df[df['vaccines'] == i].index]
    
vaccines = {}
for key,val in d.items():
    vaccines[key] = set(val)
    
for i,j in vaccines.items():
    print(f"{i}:>>{j}")


# #### Data visualization to see which countries are using the vaccines mentioned in the data

# In[10]:


import plotly.express as px
import plotly.offline as py

map_vaccine = px.choropleth(data,locations = 'iso_code',color = 'vaccines')
map_vaccine.update_layout(height = 400,margin={"r":0,"t":0,"l":0,"b":0})
map_vaccine.show()


# In[ ]:




