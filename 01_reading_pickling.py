
# coding: utf-8

# In[1]:


import pandas as pd


# ## Dataset information
# 
# This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. Many customers of the company are wholesalers.

# ### Attribute Information
# 
# InvoiceNo: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation.
# 
# StockCode: Product (item) code. Nominal, a 5-digit integral number uniquely assigned to each distinct product.
# 
# Description: Product (item) name. Nominal.
# 
# Quantity: The quantities of each product (item) per transaction. Numeric.
# 
# InvoiceDate: Invice Date and time. Numeric, the day and time when each transaction was generated.
# 
# UnitPrice: Unit price. Numeric, Product price per unit in sterling.
# 
# CustomerID: Customer number. Nominal, a 5-digit integral number uniquely assigned to each customer.
# 
# Country: Country name. Nominal, the name of the country where each customer resides.

# In[2]:


retail_df = pd.read_excel('./Online Retail.xlsx')
retail_df


# In[ ]:


pd.to_pickle(retail_df, './retail_df.pkl')

