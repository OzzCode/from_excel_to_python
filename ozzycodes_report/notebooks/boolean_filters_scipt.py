#!/usr/bin/env python
# coding: utf-8

# ## Using Boolean Filters (similar to the filter in Excel)

# In[1]:


import pandas as pd


# In[2]:


src_file = '../data/raw/sample_sales_details.xlsx'
df = pd.read_excel(src_file)
print(df.head(10))


# In[4]:


viva = df['company'] == 'Viva'
print(viva)


# In[5]:


df.loc[viva, :]


# In[6]:


print(df[viva])


# In[7]:


qty_10 = (df['quantity'] >= 10)
print(qty_10)


# In[8]:


df.loc[(qty_10 & viva), :]


# In[ ]:




