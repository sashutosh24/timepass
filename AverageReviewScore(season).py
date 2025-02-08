import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/Review500.xlsx'
data = pd.read_excel(file_path)

# Convert the Time column (UNIX timestamp) to a readable datetime format
data['Time'] = pd.to_datetime(data['Time'], unit='s')

# Extract the year-month for grouping
data['Year-Month'] = data['Time'].dt.to_period('M')

# Group by Year-Month and calculate the average Score
monthly_average_score = data.groupby('Year-Month')['Score'].mean()

# Plotting the monthly trend
plt.figure(figsize=(12, 6))
plt.plot(monthly_average_score.index.astype(str), monthly_average_score.values, marker='o', color='orange')

# Add titles and labels
plt.title('Monthly Trend of Average Review Scores Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Review Score', fontsize=12)

# Customize x-axis ticks for readability
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()
