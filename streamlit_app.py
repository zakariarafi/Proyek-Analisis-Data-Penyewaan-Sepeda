import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import seaborn as sns
import numpy as np  # untuk clustering

# Load data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Informasi Proyek
st.title('Proyek Analisis Data: Bike Sharing Data Analysis')

# Plotting
plt.figure(figsize=(10, 5)) 
sns.lineplot(data=day_df, x='dteday', y='cnt', hue='yr', palette="viridis")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # format tanggal
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonthday=-1, interval=3))  # label untuk tiap 3 bulan
plt.xticks(rotation=45)  # readability
plt.title("Tren Penyewaan Sepeda Harian Sepanjang Tahun")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(plt)

# Plotting distribusi penyewaan sepeda per jam
plt.figure(figsize=(10, 5)) 
sns.boxplot(data=hour_df, x='hr', y='cnt', palette="viridis")
plt.title('Distribusi Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Mengkategorikan jam berdasarkan jumlah penyewaan
hour_df['rental_category'] = pd.cut(hour_df['cnt'], bins=[0, 50, 100, np.inf], labels=['Low', 'Medium', 'High'])

# Mengkategorikan hari berdasarkan jumlah penyewaan
day_df['rental_category'] = pd.cut(day_df['cnt'], bins=[0, 1000, 2000, np.inf], labels=['Low', 'Medium', 'High'])

# Menampilkan hasil kategorisasi
print(hour_df[['hr', 'cnt', 'rental_category']].head())
print(day_df[['dteday', 'cnt', 'rental_category']].head())

# Plotting the distribution of rental categories throughout the day
sns.countplot(data=hour_df, x='hr', hue='rental_category', palette='viridis')
plt.title('Distribusi Kategori Penyewaan Sepanjang Hari.')
plt.xlabel('Hour of the Day')
plt.ylabel('Count')
st.pyplot(plt)
