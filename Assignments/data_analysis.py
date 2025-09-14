import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


# Set plot style
plt.style.use('seaborn-v0_8')

try:
    # Task 1: Load and Explore the Dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("First five rows of the dataset:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # No cleaning necessary as there are no missing values or incorrect types

    # Task 2: Basic Data Analysis
    print("\nBasic statistics:")
    print(df.describe())

    print("\nMean values grouped by species:")
    print(df.groupby('species').mean())

    # Task 3: Data Visualization

    # Simulate time-series by adding a time index
    df['time'] = pd.date_range(start='2022-01-01', periods=len(df), freq='D')
    df_sorted = df.sort_values('time')

    # Line chart: sepal length over time
    plt.figure(figsize=(10, 6))
    for species in df_sorted['species'].unique():
        subset = df_sorted[df_sorted['species'] == species]
        plt.plot(subset['time'], subset['sepal length (cm)'], label=species)
    plt.title('Sepal Length Over Time by Species')
    plt.xlabel('Time')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('iris_line_chart.png')
    plt.close()

    # Bar chart: average petal length per species
    plt.figure(figsize=(8, 6))
    sns.barplot(x='species', y='petal length (cm)', data=df, estimator=np.mean)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.tight_layout()
    plt.savefig('iris_bar_chart.png')
    plt.close()

    # Histogram: sepal length
    plt.figure(figsize=(8, 6))
    sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('iris_histogram.png')
    plt.close()

    # Scatter plot: sepal length vs petal length
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('iris_scatter_plot.png')
    plt.close()

except Exception as e:
    print(f"An error occurred: {e}")
