import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dataframe = pd.read_csv("Zomato data .csv")
print("Initial Data Preview:\n", dataframe.head())

# Clean and convert 'rate' column to numeric
def handleRate(value):
    try:
        return float(str(value).split('/')[0])
    except:
        return np.nan

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print("\nData After Cleaning 'rate' Column:\n", dataframe.head())

# Basic dataset info
print("\nDataset Info:\n")
dataframe.info()

# Plot: Count of different restaurant types
plt.figure(figsize=(10, 5))
sns.countplot(x='listed_in(type)', data=dataframe)
plt.xlabel("Type of Restaurant")
plt.ylabel("Count")
plt.title("Count of Restaurant Types")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total votes by restaurant type
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
grouped_data.plot(kind='line', color='green', marker='o')
plt.xlabel('Type of Restaurant', color='red', fontsize=12)
plt.ylabel('Total Votes', color='red', fontsize=12)
plt.title('Votes by Restaurant Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Restaurant(s) with maximum votes
max_votes = dataframe['votes'].max()
top_restaurants = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print('\nRestaurant(s) with the Maximum Votes:')
print(top_restaurants)

# Plot: Online order availability
plt.figure(figsize=(5, 4))
sns.countplot(x='online_order', data=dataframe, palette='Set2')
plt.title('Online Order Availability')
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Plot: Rating distribution
plt.figure(figsize=(6, 4))
plt.hist(dataframe['rate'].dropna(), bins=5, color='skyblue', edgecolor='black')
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Plot: Cost for two people
plt.figure(figsize=(8, 4))
sns.countplot(x='approx_cost(for two people)', data=dataframe, palette='Set3')
plt.title('Preferred Cost Range for Two')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot: Online order vs ratings
plt.figure(figsize=(6, 5))
sns.boxplot(x='online_order', y='rate', data=dataframe, palette='pastel')
plt.title('Online Order vs Rating')
plt.tight_layout()
plt.show()

# Heatmap: Online order across restaurant types
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Restaurant Type vs Online Order')
plt.xlabel('Online Order')
plt.ylabel('Restaurant Type')
plt.tight_layout()
plt.show()
