
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


retail_df = pd.read_pickle("./retail_df.pkl")
retail_df.head()


# Seperating cancelled orders

# In[3]:


cancelled_order_list = [False] * len(retail_df.InvoiceNo)

for i in range(len(retail_df.InvoiceNo)):
    if type(retail_df.InvoiceNo.iloc[i]) == str and retail_df.InvoiceNo.iloc[i].startswith('C'):
        cancelled_order_list[i] = True

retail_df['CancelledOrder'] = pd.Series(cancelled_order_list, index=retail_df.index)


# In[9]:


cancelled_df = retail_df[retail_df.CancelledOrder]


# In[17]:


cancelled_df.head()


# In[15]:


cancelled_df.Quantity = abs(cancelled_df.Quantity)


# In[16]:


cancelled_df.Quantity.describe()

