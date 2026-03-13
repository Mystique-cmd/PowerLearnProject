# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import kagglehub

# Download latest version
path = kagglehub.dataset_download("allen-institute-for-ai/CORD-19-research-challenge")

print("Path to dataset files:", path)

# Load metadata.csv
df = pd.read_csv(path)

# Preview structure
print(df.head())
print(df.info())

# Dimensions
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Data types
print(df.dtypes)

# Missing values
missing_summary = df.isnull().sum().sort_values(ascending=False)
print(missing_summary)

# Basic stats
print(df.describe())

# Drop columns with excessive missing data
threshold = 0.5
df_clean = df.loc[:, df.isnull().mean() < threshold]

# Fill or drop remaining NaNs
df_clean = df_clean.dropna(subset=['title', 'abstract', 'publish_time'])

# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')

# Extract year
df_clean['year'] = df_clean['publish_time'].dt.year

# Abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(str(x).split()))

# Publications per year
year_counts = df_clean['year'].value_counts().sort_index()
year_counts.plot(kind='bar', title='Publications by Year')
plt.show()

# Top journals
top_journals = df_clean['journal'].value_counts().head(10)
top_journals.plot(kind='barh', title='Top Publishing Journals')
plt.show()

# Word frequency in titles
from collections import Counter
import re

def tokenize(text):
    return re.findall(r'\b\w+\b', str(text).lower())

word_freq = Counter()
df_clean['title'].dropna().apply(lambda x: word_freq.update(tokenize(x)))

# Word cloud
wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(word_freq.most_common(100)))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.show()

# Source distribution
df_clean['source_x'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Source Distribution')
plt.show()

st.title("CORD-19 Metadata Explorer")
st.write("Explore COVID-19 research metadata interactively.")

# Widgets
year = st.slider("Select Year", int(df['year'].min()), int(df['year'].max()))
filtered = df[df['year'] == year]

st.write(f"Showing {len(filtered)} papers from {year}")
st.dataframe(filtered[['title', 'journal', 'publish_time']].head(10))

# Visualizations
st.subheader("Top Journals")
st.bar_chart(filtered['journal'].value_counts().head(10))

st.subheader("Word Cloud of Titles")
word_freq = Counter()
filtered['title'].dropna().apply(lambda x: word_freq.update(tokenize(x)))
wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(word_freq.most_common(100)))
st.image(wc.to_array())
# Drop columns with excessive missing data
threshold = 0.5
df_clean = df.loc[:, df.isnull().mean() < threshold]

# Fill or drop remaining NaNs
df_clean = df_clean.dropna(subset=['title', 'abstract', 'publish_time'])

# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')

# Extract year
df_clean['year'] = df_clean['publish_time'].dt.year

# Abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].apply(lambda x: len(str(x).split()))
