import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sb
import statistics as sta
import matplotlib.pyplot as py
import streamlit as st

df = pd.read_csv('aircrashesFull_2024.csv')
df.head()
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['Quarter'] = df['Quarter'].astype('category')
print(df['Aircraft'].value_counts().head())
st.title("Aeroplane Accidents Data")

st.header('Airplane Crashes By Quater')
py.figure(figsize=(10,6))
py.bar(df['Quarter'], df['Fatalities (air)'], color='brown')
py.xlabel('Quarter')
py.ylabel('Fatalities (air)')
py.title('Fatalities (air) by  Quarter')
py.xticks(rotation=45)  # rotate x-axis labels
py.grid(True, axis='y')  # add grid on y-axis
py.show()
st.pyplot(py)

st.header('Air plane Crash Per Incident')
# Create a histogram of fatalities (air)
# Create a figure and axis object
fig, ax = py.subplots()

# Create a histogram of fatalities (air) using the axis object
ax.hist(df['Fatalities (air)'], bins=25, edgecolor='black', color='brown', range=(0, 200))

# Set title and labels using the axis object
ax.set_title('Histogram of Fatalities (Air) per Incident')
ax.set_xlabel('Number of Fatalities')
ax.set_ylabel('Frequency')

# Show the plot
py.show()
st.pyplot(py)

location_fatalities = df.groupby('Location')['Fatalities (air)'].sum().reset_index()
top_10_locations = location_fatalities.sort_values('Fatalities (air)', ascending=False).head(10)
 #Create a bar chart
st.header('Top Ten Highest Airplane Crash')
py.figure(figsize=(10, 6))
py.barh(top_10_locations['Location'], top_10_locations['Fatalities (air)'], color='brown')
py.xlabel('Fatalities')
py.ylabel('Location')
py.title('Top 10 Locations with Highest Number of Fatalities')
py.show()
st.pyplot(py)

df = pd.read_csv('aircrashesFull_2024.csv')
st.sidebar.header('Filter Data')
Years = st.sidebar.multiselect('Select Year(s)', options=df['Year'].unique(), default=df['Year'].unique())
filtered_df = df[df['Year'].isin(Years)]

st.header('Crashes Over Time')
Crashes_per_year = filtered_df.groupby('Year').size()
py.figure(figsize=(10,6))
py.plot(Crashes_per_year.index, Crashes_per_year.values, marker='o', linestyle='-', color='brown')
py.title('Number Of Crashes Per Year')
py.xlabel('Year')
py.ylabel('Number of Crashes')
st.pyplot(py)

df['Fatalities (air)'] = df['Fatalities (air)'].astype(int)
st.header('Crashes By Month')
py.figure(figsize=(10,6))
py.bar(df['Month'], df['Fatalities (air)'], color='brown')
py.xlabel('Month')
py.ylabel('Fatalities (air)')
py.title('Fatalities (air) by Month')
py.xticks(rotation=45)  # rotate x-axis labels
py.grid(True, axis='y')  # add grid on y-axis
py.show()
st.pyplot(py)
  
