import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/Review500.xlsx'
data = pd.read_excel(file_path)

# Convert the Time column (UNIX timestamp) to a readable datetime format
data['Time'] = pd.to_datetime(data['Time'], unit='s')

# Extract the week from the Time column
data['Week'] = data['Time'].dt.to_period('W').astype(str)

# Group by Week and count the number of reviews
weekly_reviews = data.groupby('Week').size()

# Plotting the weekly trend
plt.figure(figsize=(12, 6))
plt.plot(weekly_reviews.index, weekly_reviews.values, marker='o', color='orange', linestyle='-')

# Add titles and labels
plt.title('Weekly Trend of Reviews Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Reviews', fontsize=12)

# Customize x-axis ticks for readability
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()
