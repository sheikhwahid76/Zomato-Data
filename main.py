import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
dataframe = pd.read_csv("Zomato data.csv")
print("Initial Data:")
print(dataframe.head())

# Verify column names
print("\nColumns in the DataFrame:")
print(dataframe.columns)

# Handle the 'Rating' column (instead of 'rate')
def handleRate(value):
    try:
        value = str(value).split('/')[0]  # Only take the first part if the format is 'x/y'
        return float(value)
    except Exception as e:
        print(f"Error processing value: {value} - {e}")
        return np.nan  # Handle any errors gracefully

# Apply the 'handleRate' function to the 'Rating' column and create the 'rate' column
dataframe['rate'] = dataframe['Rating'].apply(handleRate)
print("\nData with new 'rate' column:")
print(dataframe.head())

# Save the updated DataFrame back to the CSV file
dataframe.to_csv("Zomato data.csv", index=False)
print("\nCSV file has been updated and saved.")

# Display data information
dataframe.info()

# Count plot for 'Location' column
sns.countplot(x=dataframe['Location'])
plt.xlabel("Location")
plt.title('Restaurant Locations')
plt.show()

# Ratings distribution
plt.hist(dataframe['rate'], bins=5)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Get restaurant(s) with the maximum rating
max_rate = dataframe['rate'].max()
restaurant_with_max_rate = dataframe.loc[dataframe['rate'] == max_rate, 'Restaurant']
print(f"\nRestaurant(s) with the maximum rating ({max_rate}):")
print(restaurant_with_max_rate)

# Box plot of 'Location' vs. 'rate'
plt.figure(figsize=(6, 6))
sns.boxplot(x='Location', y='rate', data=dataframe)
plt.title('Box Plot of Ratings by Location')
plt.show()

# Example: Pivot table and heatmap for 'Location' vs. 'Online Order'
# Assuming 'Online Order' column exists in your dataset, like 'Yes'/'No' for online ordering
if 'Online Order' in dataframe.columns:
    pivot_table = dataframe.pivot_table(index='Location', columns='Online Order', aggfunc='size', fill_value=0)
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
    plt.title('Heatmap for Online Orders by Location')
    plt.xlabel('Online Order')
    plt.ylabel('Location')
    plt.show()
else:
    print("\n'Online Order' column is missing in the dataset, skipping the pivot table and heatmap.")