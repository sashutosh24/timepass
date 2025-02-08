import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/Review500.xlsx'
data = pd.read_excel(file_path)

# Combine all reviews into a single string
text = ' '.join(data['Text'].dropna())

# Generate the word cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    max_words=200,
    stopwords=None
).generate(text)

# Plot the word cloud
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.title('Most Common Words in Reviews', fontsize=16)
plt.tight_layout()
plt.show()
