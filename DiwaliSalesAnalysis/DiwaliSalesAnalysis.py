# %% [markdown]
# Diwali Sales Analysis

# %% [markdown]
# Introduction
# 
# Diwali, the festival of lights, not only illuminates homes but also sparks a significant surge in sales across various sectors. From consumer electronics to apparel, from sweets to home décor, businesses witness a substantial increase in transactions during this festive season. In this project, we embark on an Exploratory Data Analysis (EDA) journey to delve into the intricacies of Diwali sales data.
# 

# %% [markdown]
# Need For EDA on this dataset
# 
# Exploratory Data Analysis (EDA) serves as the foundation for understanding the underlying patterns, trends, and anomalies within a dataset. In the context of Diwali sales, EDA plays a crucial role in unraveling several key aspects:
# 
# 1. Identifying Trends: EDA helps in identifying sales trends over the years. Understanding these trends is vital for businesses to make informed decisions regarding inventory management, marketing strategies, and resource allocation.
# 
# 2. Seasonal Variation Analysis: Diwali sales are subject to seasonal fluctuations. EDA enables us to analyze the seasonal variations in sales patterns, thereby facilitating businesses in anticipating and preparing for peak demand periods.
# 
# 3. Customer Behavior Insights: By analyzing customer purchasing patterns during Diwali, businesses can gain valuable insights into consumer behavior. EDA helps in segmenting customers based on their preferences, purchase history, and demographics, thereby enabling targeted marketing campaigns.
# 
# 4. Product Performance Evaluation: EDA allows businesses to evaluate the performance of different products during Diwali sales. By examining factors such as sales volume, revenue generation, and profitability, businesses can identify top-performing products and optimize their product offerings accordingly.
# 
# 5. Competitor Analysis: EDA provides valuable insights into the competitive landscape during Diwali sales. By comparing sales data across competitors, businesses can benchmark their performance, identify areas of improvement, and devise competitive strategies.

# %% [markdown]
# Import Python Libraries

# %%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# %% [markdown]
# Import csv file

# %%
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')

# %%
df.shape

# %%
df.head()

# %%
df.info()

# %% [markdown]
# Drop Status and unnamed1 as is they are unrelated/blank columns

# %%
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# %% [markdown]
# Check for null values and drop them

# %%
pd.isnull(df).sum()
df.dropna(inplace=True)

# %% [markdown]
# Change Data Types

# %%
df['Amount'] = df['Amount'].astype('int')

# %%
df.columns

# %% [markdown]
# Getting the description of the data in the DataFrame 

# %%
df.describe()

# %%
df[['Age', 'Orders', 'Amount']].describe()

# %% [markdown]
# Plotting a bar chart for Gender and it's count

# %%
ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)

# %% [markdown]
# Plotting a bar chart for gender vs total amount

# %%
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

# %%
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)

# %% [markdown]
# Total Amount vs Age Group

# %%
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)

# %% [markdown]
# Total number of orders from top 10 states

# %%
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')

# %% [markdown]
# Total amount/sales from top 10 states

# %%
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')

# %% [markdown]
# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# %%
ax = sns.countplot(data = df, x = 'Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)

# %%
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')

# %% [markdown]
# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# %%
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)

# %%
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')

# %% [markdown]
# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# %%
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)

# %%
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

# %% [markdown]
# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category
# 

# %%
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')

# %% [markdown]
# Top 10 most sold products

# %%
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


