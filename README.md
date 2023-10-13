# Proyek Analisis Data Penyewaan Sepeda

## Informasi Umum

**Nama**: Zakaria Rafi  
**Email**: zakariarafifahmi@gmail.com  
**Id Dicoding**: zakaria_rafit

## Deskripsi Projek

Projek ini berfokus pada analisis data penyewaan sepeda untuk mendapatkan wawasan mengenai pola dan tren penyewaan sepeda. Dua dataset utama yang digunakan adalah `day.csv` dan `hour.csv`, yang berisi data harian dan jam penyewaan sepeda.

## Pertanyaan Bisnis

1. Bagaimana pola penyewaan sepeda harian berubah sepanjang tahun, dan apakah ada pola musiman?
2. Pada jam berapa dalam sehari jumlah penyewaan sepeda mencapai puncaknya?

## Analisis Data

Analisis data dilakukan dengan menggunakan Python dan berbagai library seperti pandas, matplotlib, dan seaborn. Proses analisis meliputi eksplorasi data, visualisasi, dan interpretasi hasil untuk menjawab pertanyaan bisnis.

### Teknik Analisis Lanjutan

Teknik clustering digunakan untuk lebih memahami pola penyewaan sepeda dan mengelompokkan data berdasarkan karakteristik tertentu.

## Dashboard

Dashboard interaktif dibuat dengan menggunakan Streamlit untuk memvisualisasikan hasil analisis data secara interaktif. Dashboard dapat diakses [https://appapp-f4zxv5trpt74jgcbhczrw4.streamlit.app/]

## Setup Environment
Anda perlu membuat environment khusus menggunakan Conda dan menginstall dependensi yang diperlukan. Ikuti langkah-langkah berikut:

```

conda create --name main-ds python=3.9
conda activate main-ds
pip install streamlit pandas numpy matplotlib seaborn
```
## Run steamlit app
```streamlit run streamlit_app.py