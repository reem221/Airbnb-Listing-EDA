import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/listings.csv')
df.head()

df.info()
df.describe()
df.describe(include=['object','bool'])
df.isnull().sum()
df.shape
df.columns

df.drop(['neighbourhood_group_cleansed','calendar_updated','license'], axis=1, inplace=True)

df['price'] = df['price'].astype('category')
df.head()

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], kde=True)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='longitude', y='latitude', hue='price', data=df, palette='viridis')
plt.title('Price Distribution by Location')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='availability_365', y='price', data=df)
plt.title('Price vs. Availability')
plt.xlabel('Availability (365 days)')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(12,8))
sns.boxplot(x='neighbourhood',y='price',data=df)

plt.figure(figsize=(30,30))
sns.boxplot(x='property_type',y='price',data=df)

data = df.select_dtypes(include='number')
plt.figure(figsize=(30,30))
sns.heatmap(data.corr(),annot=True)