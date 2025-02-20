import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data (assuming the CSV file generated previously)
df = pd.read_csv('src_files/f1_lap_times_with_edge_cases.csv')

# Step 1: Remove empty values (NaN or None)
df_cleaned = df.dropna(subset=['Time'])  # Drop rows where 'Time' is NaN
df_cleaned = df_cleaned.dropna(subset=['Driver']) # Drop rows where 'Driver' is NaN

# Step 2: Remove rows with wrong data types (non-numeric lap times)
# Convert 'Time' column to numeric, coercing errors into NaN, then drop those rows
df_cleaned['Time'] = pd.to_numeric(df_cleaned['Time'], errors='coerce')
df_cleaned = df_cleaned.dropna(subset=['Time'])

# Remove rows where 'Driver' is a number
df_cleaned = df_cleaned[~df_cleaned['Driver'].apply(lambda x: x.isdigit())]


# Step 3: Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Step 4: Remove outliers

#remove values that are below a threshold. in my case, I will set the threshold to 1

df_cleaned = df_cleaned[df_cleaned['Time'] > 1] 

#Identify and remove outliers using both Z-score and IQR

# Z-score method:
z_scores = stats.zscore(df_cleaned['Time'])
threshold_z = 3  # Set a strict threshold for Z-scores
df_cleaned = df_cleaned[np.abs(z_scores) < threshold_z]

# IQR method:
Q1 = df_cleaned['Time'].quantile(0.25)
Q3 = df_cleaned['Time'].quantile(0.75)
IQR = Q3 - Q1

# Define upper and lower bounds for detecting outliers using IQR
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove rows where 'Time' is outside of the IQR bounds
df_cleaned = df_cleaned[(df_cleaned['Time'] >= lower_bound) & (df_cleaned['Time'] <= upper_bound)]


driver_counts = df_cleaned.groupby('Driver').size()

valid_drivers = driver_counts[driver_counts >= 3].index
df_cleaned = df_cleaned[df_cleaned['Driver'].isin(valid_drivers)] #Filter the DataFrame to include only these valid drivers

#Check if we have at least 10 drivers
if df_cleaned['Driver'].nunique() < 10:
    raise ValueError("Not enough drivers with at least 3 lap times. You need at least 10 drivers.")


df_cleaned.to_csv('src_files/f1_lap_times_cleaned.csv', index=False)