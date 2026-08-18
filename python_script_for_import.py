import kagglehub

# Using Kaggle API
# Download latest version to the environment
path = kagglehub.dataset_download("emmanuelfwerr/london-weather-data")

print("Path to dataset files:", path)

import os

# List all files in the environment directory
files = os.listdir(path)
print(files)

import pandas as pd

# Selecting our data file from the environment directory
file_name = "london_weather.csv" # Replace with your actual file name
full_path = os.path.join(path, file_name)

# Load data file into a pandas DataFrame
df = pd.read_csv(full_path)

#Converting the 'date' column, which is currently a string variable, into a date time variable to split the column into day/month/year
df['date_converted'] = pd.to_datetime(df['date'].astype(str), format='%Y%m%d')

#Creating separate columns for the month value, day value, and year value in the 'date' column
df['day'] = df['date_converted'].dt.day
df['month'] = df['date_converted'].dt.month
df['year'] = df['date_converted'].dt.year

# Filtering data to represent only the year 1979. This is for a quick example of data manipulation
df_1982_filter = df.loc[df['year'] == 1982]

# Grouping the filtered data by the 'month' column and taking the average of the 'precipitation'. This way we can look at average percipation per month in 1979

import matplotlib.pyplot as plt

# Grouping my 'month' and averaging 'percipitation' - creating bar plot to visualize the data
df_1982_filter.groupby('month')['precipitation'].mean().plot(kind='bar', color='skyblue', rot=0)

# Customizing and displaying the plot
plt.title('Average Precipitation by Month (mm) in 1982')
plt.ylabel('Average Snow Depth')
plt.xlabel('Month')
plt.show()
plt.savefig('output_plot.png') 
