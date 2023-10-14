import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
import seaborn as sns
import numpy as np  # untuk clustering

# Informasi Proyek
st.title('Proyek Analisis Data: Bike Sharing Data Analysis')

'''
# Load data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

st.markdown("""
- **Nama:** Zakaria Rafi
- **Email:** zakariarafifahmi@gmail.com
- **ID Dicoding:** zakaria_rafi
""")

st.subheader('Menentukan Pertanyaan Bisnis')

st.write("""
- **Pertanyaan 1:** Bagaimana pola penyewaan sepeda harian berubah sepanjang tahun, dan apakah ada pola musiman?
- **Pertanyaan 2:** Pada jam berapa dalam sehari jumlah penyewaan sepeda mencapai puncaknya?
""")

# Option to select data view
option = st.selectbox('Select Data', ('Day Data', 'Hour Data'))
if option == 'Day Data':
    st.write(day_df)
elif option == 'Hour Data':
    st.write(hour_df)


# Menambahkan kesimpulan pertanyaan 1
st.subheader('Kesimpulan Pertanyaan 1:')
st.write("""
Ada pola musiman dalam penyewaan sepeda, dengan peningkatan penyewaan sekitar April hingga September (bulan-bulan hangat).
Tren penyewaan menunjukkan peningkatan dari tahun ke tahun.
""")

'''

# Plotting+pallette
plt.figure(figsize=(10, 5)) 
sns.lineplot(data=day_df, x='dteday', y='cnt', hue='yr', palette="viridis")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # format tanggal
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonthday=-1, interval=3))  # label untuk tiap 3 bulan
plt.xticks(rotation=45) #readability
plt.title("Tren Penyewaan Sepeda Harian Sepanjang Tahun")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(plt)

'''
# Menambahkan kesimpulan pertanyaan 2
st.subheader('Kesimpulan Pertanyaan 2:')
st.write("""
Ada dua puncak penyewaan sepeda dalam sehari, yang berkorelasi dengan jam berangkat dan pulang kerja.
Optimalisasi ketersediaan sepeda pada jam-jam sibuk dapat meningkatkan layanan kepada pelanggan.
""")
'''

# Plotting distribusi penyewaan sepeda per jam+pallette
plt.figure(figsize=(10, 5)) 
sns.boxplot(data=hour_df, x='hr', y='cnt', palette="viridis")
plt.title('Distribusi Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

'''
# Menambahkan Teknik Analisis Lanjutan
st.subheader('Teknik Analisis Lanjutan: Clustering')
st.write("""
Setelah menganalisis dan mendapatkan kesimpulan mengenai data penyewaan sepeda, kita akan menerapkan teknik clustering untuk lebih memahami pola penyewaan sepeda dan mengelompokkan data berdasarkan karakteristik tertentu.
""")
'''

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
