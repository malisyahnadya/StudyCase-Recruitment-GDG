# StudyCase-Recruitment-GDG: Proyek Analisis Data E-Commerce

Oleh: **Malisyah Nadya Marvini**

## Deskripsi Proyek
Proyek ini bertujuan untuk melakukan eksplorasi data (EDA) pada dataset publik e-commerce dalam menganalisis performa bisnis e-commerce dengan fokus pada pemetaan demografis pelanggan dan optimasi kategori produk. Dashboard ini dikembangkan untuk memberikan insight visual bagi pengambil keputusan bisnis mengenai konsentrasi pasar dan kategori produk yang paling menguntungkan.

## Dataset yang Digunakan
Dataset yang digunakan berasal dari **E-Commerce Public Dataset** 
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Ringkasan Insight Hasil Analisis

Berdasarkan dashboard interaktif yang telah disusun, berikut adalah beberapa temuan kunci:

1. **Dominasi Pasar**:
- Kota **São Paulo** secara signifikan memiliki jumlah customer unik terbanyak. Hal ini mengindikasikan bahwa infrastruktur e-commerce dan konsumsi masyarakat paling terkonsentrasi di wilayah tersebut. 
2. **Perbandingan Penjualan vs Pendapatan**:
- Kategori **cama_mesa_banho** tertinggi dalam jumlah unit yang terjual. 
- Berdasarkan grafik, **beleza_saude** adalah kategori dengan pendapatan tertinggi. Hal ini mengindikasikan produk yang paling banyak terjual ternyata tidak selalu menghasilkan pendapatan paling banyak.

## Cara Menjalankan Notebook dan Dashboard

### 1. Menjalankan Notebook (.ipynb)
- Pastikan library `pandas`dan `matplotlib` telah terinstal.
- Jalankan file notebook analisis langkah demi langkah untuk melihat proses pengolahan data.

### 2. Menjalankan Dashboard Streamlit (Lokal)
Pastikan file `dashboard.py`, `data_ecommerce.csv`, dan `requirements.txt` berada dalam folder yang sama:
1. Instal library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   
2. Jalankan dashboard:
   ```bash
   streamlit run dashboard.py
