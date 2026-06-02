#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np
import logging
import warnings

warnings.filterwarnings("ignore")


# In[84]:


excel_file = "/kaggle/input/datasets/purnimasatish/usecase/USECASE - Data Engineering.xlsx"

xls = pd.ExcelFile(excel_file)

print(xls.sheet_names)


# In[85]:


retail1 = pd.read_excel(
    excel_file,
    sheet_name='retail_data1'
)

retail2 = pd.read_excel(
    excel_file,
    sheet_name='retail_data2'
)

product_dim = pd.read_excel(
    excel_file,
    sheet_name='product_details'
)

print("Retail1 Shape:", retail1.shape)
print("Retail2 Shape:", retail2.shape)
print("Product Dimension Shape:", product_dim.shape)


# In[86]:


print(retail1.columns.tolist())
print(retail2.columns.tolist())
print(product_dim.columns.tolist())


# In[87]:


print(retail1.columns)
print(retail2.columns)


# In[88]:


retail_df = pd.concat(
    [retail1, retail2],
    ignore_index=True
)

print("Combined Successfully")
print(retail_df.shape)


# In[89]:


print(retail_df.shape)

retail_df.head()


# In[90]:


retail_df.info()


# In[91]:


retail_df.isnull().sum()


# In[92]:


retail_df.duplicated().sum()


# In[93]:


before = retail_df.shape[0]

retail_df.drop_duplicates(inplace=True)

after = retail_df.shape[0]

print("Duplicates Removed:", before-after)


# In[94]:


print(product_dim.columns)

price_lookup = product_dim.set_index("product_id")["price"]

category_lookup = product_dim.set_index("product_id")["category"]

product_lookup = product_dim.set_index("product_id")["product_name"]


# In[95]:


retail_df['price'] = retail_df['price'].fillna(
    retail_df['product_id'].map(price_lookup)
)


# In[96]:


retail_df['category'] = retail_df['category'].fillna(
    retail_df['product_id'].map(category_lookup)
)


# In[97]:


retail_df['product_name'] = retail_df['product_name'].fillna(
    retail_df['product_id'].map(product_lookup)
)


# In[98]:


retail_df.fillna("Unknown", inplace=True)


# In[99]:


retail_df['product_name'] = (
    retail_df['product_name']
    .astype(str)
    .str.strip()
    .str.title()
)


# In[100]:


retail_df['category'] = (
    retail_df['category']
    .astype(str)
    .str.strip()
    .str.title()
)


# In[101]:


retail_df['city'] = (
    retail_df['city']
    .astype(str)
    .str.strip()
    .str.title()
)


# In[102]:


retail_df['payment_method'] = (
    retail_df['payment_method']
    .astype(str)
    .str.strip()
    .str.upper()
)


# In[103]:


retail_df['payment_status'] = (
    retail_df['payment_status']
    .astype(str)
    .str.strip()
    .str.title()
)


# In[104]:


retail_df['transaction_date'] = pd.to_datetime(
    retail_df['transaction_date'],
    errors='coerce'
)


# In[105]:


retail_df = retail_df[
    retail_df['quantity'] > 0
]


# In[106]:


retail_df = retail_df[
    retail_df['price'] > 0
]


# In[107]:


def mask_email(email):
    email = str(email)

    if '@' in email:
        name, domain = email.split('@')
        return name[:3] + '****@' + domain

    return email

retail_df['masked_email'] = retail_df['email'].apply(mask_email)


# In[108]:


def mask_phone(phone):

    phone = str(phone)

    if len(phone) >= 4:
        return 'XXXXXX' + phone[-4:]

    return phone

retail_df['masked_phone'] = retail_df['phone'].apply(mask_phone)


# In[109]:


retail_df.drop(
    columns=['email','phone'],
    inplace=True
)


# In[110]:


retail_df['product_name'] = retail_df['product_id'].map(product_lookup)

retail_df['category'] = retail_df['product_id'].map(category_lookup)

retail_df['price'] = retail_df['product_id'].map(price_lookup)


# In[111]:


retail_df['revenue'] = (
    retail_df['price']
    * retail_df['quantity']
    * (1 - retail_df['discount']/100)
)


# In[112]:


print('revenue' in retail_df.columns)


# In[113]:


retail_df[
    ['product_name',
     'price',
     'quantity',
     'discount',
     'revenue']
].head()


# In[114]:


total_revenue = retail_df['revenue'].sum()

print("Total Revenue:", round(total_revenue,2))


# In[115]:


revenue_by_category = retail_df.groupby(
    'category'
)['revenue'].sum().reset_index()

revenue_by_category.sort_values(
    'revenue',
    ascending=False
)


# In[116]:


revenue_by_category = retail_df.groupby(
    'city'
)['revenue'].sum().reset_index()

revenue_by_category.sort_values(
    'revenue',
    ascending=False
)


# In[117]:


top_products = retail_df.groupby(
    'product_name'
)['quantity'].sum().reset_index()

top_products.sort_values(
    'quantity',
    ascending=False
).head(10)


# In[118]:


retail_df.head()


# In[119]:


retail_df.to_csv(
    "clean_retail_sales.csv",
    index=False
)

print("Dataset Exported Successfully")

