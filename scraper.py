#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[21]:


r = requests.get('https://www.bbc.com')
doc = BeautifulSoup(r.text)


# In[22]:


titles = doc.select('.media__title a')

[title.text.strip() for title in titles]


# In[25]:


[title['href'] for title in titles]


# In[26]:


rows = []

for title in titles:
    datapoint = {}
    
    datapoint['title'] = title.text.strip()
    
    datapoint['url'] = title['href']
    
    rows.append(datapoint)
    
rows


# In[17]:


df = pd.DataFrame(rows)


# In[19]:


df.to_csv('bbc.csv', index = False)


# In[ ]:




